#!/bin/bash
ASCII="../bin/ascii.txt"
export PYTHONPATH="../:$PYTHONPATH"
for f in $(find . -type f | grep "hello_world"); do
    pyxstitch --file $f
    if [ $? -ne 0 ]; then
        echo "processing error $f"
        exit 1
    fi
done

python -c """import string; 

for ch in string.printable:
    print(ch)
""" > $ASCII
if [ $? -ne 0 ]; then
    echo "ascii test failed"
    exit
fi
pyxstitch --file $ASCII
