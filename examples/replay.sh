#!/bin/bash
OUT="outputs/"
EXIT_CODE=0
for f in $(ls ${OUT}* | grep "pyxstitch$"); do
    echo "replaying: $f"
    pyxstitch --file $f --output ../bin/replay.png
    if [ $? -ne 0 ]; then
        echo "failed..."
        EXIT_CODE=1
    fi
done
exit $EXIT_CODE
