#!/bin/bash
for i in $(seq 1 100); do
    o=""
    if [ $(($i % 3)) -eq 0 ]; then
        o="Fizz"
    fi
    if [ $(($i % 5)) -eq 0 ]; then
        o=$o"Buzz"
    fi
    if [ -z "$o" ]; then
        echo $i
    else
        echo $o
    fi
done
