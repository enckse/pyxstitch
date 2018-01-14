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
~~~~~~~~

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
