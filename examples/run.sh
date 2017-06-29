#!/bin/bash
export PYTHONPATH="../:$PYTHONPATH"
for f in $(find . -type f); do
    python ../main.py --file $f
    if [ $? -ne 0 ]; then
        exit 1
    fi
done
