pyxstitch
=========

.. image:: https://raw.githubusercontent.com/enckse/pyxstitch/master/images/pyxstitch.png


pyxstitch is an application (and associated library/compenents) that
takes source code files and produces syntax-highlighted patterns for
cross stitching.

See a examples and completed cross stitch patterns
`here! <https://enckse.github.io/pyxstitch/>`__

.. image:: https://travis-ci.org/enckse/pyxstitch.svg?branch=master
    :target: https://travis-ci.org/enckse/pyxstitch

.. image:: https://ci.appveyor.com/api/projects/status/w2mv66xci68k7hw2?svg=true
    :target: https://ci.appveyor.com/project/enckse/pyxstitch

install
-------

pip
~~~

Available via `pip <https://pypi.python.org/pypi/pyxstitch/>`__

::

    pip install pyxstitch

source
~~~~~~

-  Clone this repo and…

::

    python setup.py install

or

::

    pip install .

or

::

    pip install -e .

os packaging
~~~~~~~~~~~~

+------------+----------------------------------------------------------------+
| os         | link                                                           |
+============+================================================================+
| arch linux | `aur <https://aur.archlinux.org/packages/python-pyxstitch/>`__ |
+------------+----------------------------------------------------------------+

usage
-----

to run

::

    pyxstitch --file program.py

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
fonts
~~~~~

to select a different font (from available)

::

    pyxstitch --font <type-charset-size>

floss colors
~~~~~~~~~~~~

colors can be remapped or disabled, e.g. to disable a color, set it to
map to empty

::

    pyxstitch --file test.c --map 000000=

or to map one color to another

::

    pyxstitch --file test.c --map 000000=ffffff

advanced
--------

some configuration options are available via the ``--kv`` input
settings. Alternatively set these in a $HOME/.pyxstitch.config file to
use different defaults always (unless a ``--kv`` is passed) or pass a
``--config`` and specify a different file than the one in $HOME

::

    vim $HOME/.pyxstitch.config
    ---
    # comments will be ignored
    page_height=400
    page_width=300

height
^^^^^^

sets the default page height (600 default)

::

    --kv page_height=500
width
^^^^^

sets the default page width (1000 default)

::

    --kv page_width=900

padding
^^^^^^^

page padding (margins) which defaults to 50

::

    --kv page_pad=100

index
^^^^^

on multipage will produce an html file (by default of 0) to group images
into a pattern

::

    --kv page_no_index=1

legend
^^^^^^

default is 0, will print the legend to console (instead of to output
image) when set to 1

::

    --kv page_legend=1

height offset
^^^^^^^^^^^^^

default is 0, will change legend height placement on an image

::

    --kv legend_hoff=10

width offset
^^^^^^^^^^^^

default is 0, will change legend width placement on an image

::

    --kv legend_woff=-5

font size
^^^^^^^^^

to adjust the font scaling for the legend when in the output

::

    --kv page_font_size=100

zoom
~~~~

you can zoom the pattern in by specifying the vertical and/or horizontal
zoom start/end

::

    pyxstitch --hszoom 20 --hezoom 30 --vszoom 10 --vezoom 40

will zoom the output to horizontal grid position 20 to 30 and vertical
grid position 10 to 40

examples
--------

there are example source code files and corresponding output pngs in the
``examples`` folder

customizing
-----------

the library components of the CrossStitchFormatter can be changed such
that you can:

- Adjust how symbols for various colors are chosen (replace ``DefaultSymbolGenerator`` on the formatter) 
- Define a new font for Font creation method by adjusting ``Font``
