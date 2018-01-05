#!/bin/bash
VERS_PY="pyxstitch/version.py"
VERS=$(cat $VERS_PY | grep "__version__" | cut -d "=" -f 2 | sed 's/ //g;s/"//g' | sed "s#\.#\\\.#g")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
TAG=$(git tag -l | sort -r | head -n 1 | sed "s/v//g" | sed "s/\./\\./g")
EXAMPLES=examples/
EXAMPLE_OUT=${EXAMPLES}outputs/
NO_TAG="na"
COMPLETIONS="completions/"

_handle_version() {
    sed -i "s/$VERS/\_\_VERSION\_\_/g" $1
}

_fail() {
    if [ $1 -ne 0 ]; then
        echo "failed"
        exit 1
    fi
}

_completions() {
    _bash=$COMPLETIONS/bash
    # bash
    printf "%s" 'function _pyxstitch()
{
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
    pyxstitch --file ${EXAMPLES}/${HW}$1 --multipage off --format ${FORMAT} --output ${BIN}/${HW}$1.${FORMAT} $2 $4 $5 $6
    _fail $?
	pyxstitch --file ${BIN}/$HW$1.$FORMAT --output $BIN/$HW$1.png $2
    _fail $?
	_handle_version "$BIN/$HW$1.$FORMAT"
    _fail $?
	diff $BIN/$HW$1.$FORMAT $EXAMPLE_OUT$HW$1.$FORMAT$3
    _fail $?
}

_gen_font() {
    pyxstitch --file $EXAMPLES/$HW"ascii.txt" --quiet --theme bw --kv page_legend=1 --multipage off --output $BIN/$1.png --font $1-ascii-$2
    _fail $?
    cp $BIN/$1.png $BIN/$2.png
    _fail $?
}

_run_bash() {
    pyxstitch --file $EXAMPLES/fizzbuzz.bash --multipage off --font monospace-ascii-5x9 --format $FORMAT --output $BIN/fb.bash.$FORMAT $1
    _fail $?
    _handle_version "$BIN/fb.bash.$FORMAT"
    _fail $?
    diff $BIN/fb.bash.$FORMAT ${EXAMPLE_OUT}fb.bash.$FORMAT$2
    _fail $?
}

_ascii() {
    for f in $(_fonts); do
        ext="."$(echo $f | cut -d "-" -f 3)
        echo "ascii: $f ($ext)"
        _example "ascii.txt" "--font $f" $ext
    done
}

_build_fonts() {
    for f in $(_fonts); do
        t=$(echo "$f" | cut -d "-" -f 1)
        s=$(echo "$f" | cut -d "-" -f 3)
        echo "font generation: $f ($t,$s)"
        _gen_font $t $s
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
	diff $zoom ${EXAMPLE_OUT}zoom.$FORMAT
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
esac

if [ -z "$cmd" ]; then
    echo "unknown command: $cmd"
    exit 1
fi

$cmd "${@:2}"
