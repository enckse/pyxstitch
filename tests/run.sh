#!/bin/bash
export PYTHONPATH="../:../fonts/:$PYTHONPATH"
python -m unittest discover -p "*.py"
exit $?
