pyxstitch
===

pyxstitch is an application (and associated library/compenents) that takes source code files and produces syntax-highlighted patterns for cross stitching

[![Build Status](https://travis-ci.org/enckse/pyxstitch.svg?branch=master)](https://travis-ci.org/enckse/pyxstitch)

# install

* Clone this repository and run something to one of the following depending on system configuration:

```
python setup.py install
```
or
```
pip install .
```
or
```
pip install -e .
```

# usage

to run
```
pyxstitch --file program.py
```

to see actual highlight colors on the pattern use `--colorize` and if using a high-contrast style you may want to toggle `--dark`

the coloring styles are available as part of the pygments project but can be passed like
```
pyxstitch --file program.py --style monokai
```

by default a a png file is created matching the source code name (e.g. `hello.py` -> 'hello.png'), to change this
```
pyxstitch --file program.py --output image.png
```

# examples

there are example source code and corresponding output pngs in the `examples` folder

# customizing

the library components of the CrossStitchFormatter can be changed to:
* Adjust how symbols for various colors are chosen (replace `DefaultSymbolGenerator` on the formatter)
* Change the ascii-driven `DefaultFontFactory` by changing the formatter property

# limitations

this is a jumpstarter and lacks some useful features that could be added later:
* Does not output DMC colors
* Does not validate colors on the pattern/style/etc.
* Many other things

**Note:** Again - this is just a jump start to creating patterns for cross stitching from source code
