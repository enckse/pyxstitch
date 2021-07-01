#!/bin/bash
VERS=$(grep "version=" setup.py | cut -d "=" -f 2 | sed 's/ //g;s/"//g' | sed "s#\.#\\\.#g")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
EXAMPLES=examples/
EXAMPLE_OUT=${EXAMPLES}outputs/
RESOURCES="resources/"
MAN1="pyxstitch.1"
DOCMAN1="$RESOURCES$MAN1"

_handle_version() {
    sed -i "s/$VERS/\_\_VERSION\_\_/g" $1
}

_fail() {
    if [ $1 -ne 0 ]; then
        echo "failed"
        exit 1
    fi
}

_manpages() {
    local dated
    dated=$(git log -1 --date=format:"%B %Y" --format=%cd $DOCMAN1)
    cat $DOCMAN1 | sed "s/<Version>/$VERS/g" | sed "s/<Date>/$dated/g" > $BIN/$MAN1
    cd $BIN && gzip $MAN1
}

_completions() {
    _bash=$RESOURCES/bash.completions
    # bash
    printf "%s" '_pyxstitch() {
    local cur opts 
    if [ $COMP_CWORD -eq 1 ]; then
        cur=${COMP_WORDS[COMP_CWORD]}
        opts=$(echo "' > $_bash
    first=1
    for f in $(pyxstitch --help | sed "s/^\s*//g;s/, //g;s/^-h//g" | grep "^\-" | cut -d " " -f 1 | sort); do
        if [ $first -eq 1 ]; then
            fmt="%s"
            first=0
        else
            fmt=" %s"
        fi
        printf "$fmt" $f >> $_bash
    done
    echo '")
        COMPREPLY=( $(compgen -W "$opts" -- $cur) )
    fi
}

complete -F _pyxstitch pyxstitch' >> $_bash
}

_example() {
    pyxstitch --file ${EXAMPLES}/${HW}$1 --lexer typoscript --multipage off --format ${FORMAT} --output ${BIN}/${HW}$1.${FORMAT} $2 $4 $5 $6
    _fail $?
	pyxstitch --file ${BIN}/$HW$1.$FORMAT --output $BIN/$HW$1.png $2
    _fail $?
	_handle_version "$BIN/$HW$1.$FORMAT"
    _fail $?
	diff -u $BIN/$HW$1.$FORMAT $EXAMPLE_OUT$HW$1.$FORMAT$3
    _fail $?
}

_gen_font() {
    pyxstitch --file $EXAMPLES/$HW"ascii.txt" --quiet --theme bw --kv page_legend=1 --multipage off --output $BIN/$1.png --font $1-ascii-$2
    _fail $?
    cp $BIN/$1.png $BIN/$3.png
    _fail $?
}

_run_bash() {
    pyxstitch --file $EXAMPLES/fizzbuzz.bash --multipage off --font monospace-ascii-5x9 --format $FORMAT --output $BIN/fb.bash.$FORMAT $1
    _fail $?
    _handle_version "$BIN/fb.bash.$FORMAT"
    _fail $?
    diff -u $BIN/fb.bash.$FORMAT ${EXAMPLE_OUT}fb.bash.$FORMAT$2
    _fail $?
}

_ascii() {
    local f ext
    for f in $(_fonts); do
        ext="."$(echo $f | cut -d "-" -f 3)
        if echo "$f" | grep -q "prop"; then
            ext="${ext}p"
        fi
        echo "ascii: $f ($ext)"
        _example "ascii.txt" "--font $f" $ext
    done
}

_build_fonts() {
    local f t s m
    for f in $(_fonts); do
        t=$(echo "$f" | cut -d "-" -f 1)
        s=$(echo "$f" | cut -d "-" -f 3)
        m=$s
        if echo $f | grep -q "prop"; then
            m=${m}p
        fi
        echo "font generation: $f ($t,$s,$m)"
        _gen_font $t $s $m
    done
}

_fonts() {
    pyxstitch --help | grep "\-\-font" | head -n 1 | cut -d "{" -f 2 | cut -d "}" -f 1 | sed "s/detect//g;s/,/ /g"
}

_zoom() {
    local zoom
    zoom="$BIN/zoom.$FORMAT"
    pyxstitch --file $EXAMPLES/$HW"ascii.txt" --quiet --format $FORMAT --hszoom 7 --hezoom 17 --vszoom 12 --vezoom 50 --theme bw --kv page_legend=1 --multipage off --output $zoom
    _fail $?
    _handle_version "$zoom"
    _fail $?
	diff -u $zoom ${EXAMPLE_OUT}zoom.$FORMAT
    _fail $?
}

cmd=""
case $1 in
    "zoom")
        cmd="_zoom"
        ;;
    "example")
        cmd="_example"
        ;;
    "version")
        cmd="_handle_version"
        ;;
    "fonts")
        cmd="_build_fonts"
        ;;
    "bash")
        cmd="_run_bash"
        ;;
    "ascii")
        cmd="_ascii"
        ;;
    "completions")
        cmd="_completions"
        ;;
    "man")
        cmd="_manpages"
        ;;
esac

if [ -z "$cmd" ]; then
    echo "unknown command: $cmd"
    exit 1
fi

$cmd "${@:2}"
