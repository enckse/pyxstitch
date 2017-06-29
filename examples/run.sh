#!/bin/bash
ASCII="../bin/ascii.txt"
export PYTHONPATH="../:$PYTHONPATH"
for f in $(find . -type f | grep -v "run.sh"); do
    pyxstitch --file $f --output ../bin/$(basename $f).png
    if [ $? -ne 0 ]; then
        echo "processing error $f"
        exit 1
    fi
done
