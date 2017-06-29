#!/bin/bash
ASCII="../bin/ascii.txt"
export PYTHONPATH="../:$PYTHONPATH"
for f in $(find . -maxdepth 1 -type f | grep -v "run.sh"); do
    file_name=$(basename $f).png
    bin_file=../bin/$file_name
    pyxstitch --file $f --output $bin_file
    if [ $? -ne 0 ]; then
        echo "processing error $f"
        exit 1
    fi
    diff $bin_file outputs/$file_name
done
