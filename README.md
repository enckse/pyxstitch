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

to see actual highlight colors on the pattern use `--theme light-full` and if using a high-contrast style you may want to toggle `--theme dark` (or `--theme dark-full` for colors on dark)

the coloring styles are available as part of the pygments project but can be passed like
```
pyxstitch --file program.py --style monokai
```

by default a a png file is created matching the source code name (e.g. `hello.py` -> 'hello.png'), to change this
```
pyxstitch --file program.py --output image.png
```

or just pass a file type and type/cat into pyxstitch
```
cat test.py | pyxstitch --file .py --output myimage.png
```

by default it will use just a text (no syntax) if piped/stdin is used, that can be changed, so
```
cat test.py | pyxstich
```

produces no highlighting but
```
cat test.py | pyxstitch --file .py
# or
cat test.py | pyxstitch --lexer autodetect
# or tell it which pygments lexer to use
cat test.py | pyxstitch --lexer python
```

will chcek the syntax of the file (or attempt to)

by default, pyxstitch will attempt to create multiple pages for easier reading of large patterns, this can be modified via `--multipage`.

**Note:** When producing multiple pdfs, using ghostscript a single pdf can be merged from the results of pyxstitch

```
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf file_001.pdf file_002.pdf
```


# examples

there are example source code and corresponding output pngs in the `examples` folder

# customizing

the library components of the CrossStitchFormatter can be changed to:
* Adjust how symbols for various colors are chosen (replace `DefaultSymbolGenerator` on the formatter)
* Change the ascii-driven `DefaultFontFactory` by changing the formatter property
