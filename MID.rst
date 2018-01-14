styling
~~~~~~~

to see actual highlight colors on the pattern use ``--theme light-dmc``
and if using a high-contrast style you may want to toggle
``--theme dark`` (or ``--theme dark-dmc`` for colors on dark
backgrounds).

the coloring styles are available as part of the pygments project but
can be passed like so

::

    pyxstitch --file program.py --style monokai

output
~~~~~~

by default a png file is created matching the source code file name
(e.g. ``hello.py`` -> ``hello.png``), to change this

::

    pyxstitch --file program.py --output image.png

or just pass a file type and type/cat into pyxstitch

::

    cat test.py | pyxstitch --file .py --output myimage.png

by default, pyxstitch will attempt to create multiple pages for easier
reading of large patterns, this can be modified via ``--multipage``.

syntax/lexer
~~~~~~~~~~~~

by default pyxstitch will use just a text lexer (no syntax) if
piped/stdin is used, that can be changed, so

::

    cat test.py | pyxstich

produces no highlighting but

::

    cat test.py | pyxstitch --file .py
    # or
    cat test.py | pyxstitch --lexer autodetect
    # or tell it which pygments lexer to use
    cat test.py | pyxstitch --lexer python
