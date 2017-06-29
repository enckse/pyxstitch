#!/bin/bash
export PYTHONPATH="../:$PYTHONPATH"
python -m unittest discover -p "*.py"
exit $?
