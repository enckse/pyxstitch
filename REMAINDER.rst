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

