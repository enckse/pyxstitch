#!/bin/bash
DIST=dist/
REPO=""
if [ ! -z "$1" ]; then
    REPO="-r $1"
fi
if [ ! -d $DIST ]; then
    echo "no dist found..."
    exit 1
fi

file=$(ls $DIST | grep ".tar.gz$")
if [ -z "$file" ]; then
    echo "no package found"
    exit 1
fi
cnt=$(echo $file | wc -l)
if [ $cnt -ne 1 ]; then
    echo "unable to find unique package: $file"
    exit 1
fi
echo "going forward with: $DIST$file"
twine register $DIST$file $REPO
if [ $? -ne 0 ]; then
    echo "unable to register"
    exit 1
fi
twine upload ${DIST}* $REPO
