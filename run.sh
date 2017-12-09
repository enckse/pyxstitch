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

_handle_version() {
    sed -i "s/$VERS/\_\_VERSION\_\_/g" $1
}

_fail() {
    if [ $1 -ne 0 ]; then
        echo "failed"
        exit 1
    fi
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

cmd=""
case $1 in
    "example")
        cmd="_example"
        ;;
    "version")
        cmd="_handle_version"
        ;;
    "fonts")
        cmd="_gen_font"
        ;;
    "bash")
        cmd="_run_bash"
        ;;
esac

if [ -z "$cmd" ]; then
    echo "unknown command: $cmd"
    exit 1
fi

$cmd "${@:2}"
