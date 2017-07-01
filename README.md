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

# Characters

Characters may need re-design/rework/actual stitching to be verified. Generally something marked as 'verified' has been stitched and looks reasonable, all other labels should be self-explanatory

## Default

| Char | Status   |
| ---  | ---      |
|    0 | verified |
|    1 | verified |
|    2 | unknown  |
|    3 | unknown  |
|    4 | unknown  |
|    5 | unknown  |
|    6 | unknown  |
|    7 | unknown  |
|    8 | unknown  |
|    9 | unknown  |
|    a | unknown  |
|    b | unknown  |
|    c | unknown  |
|    d | unknown  |
|    e | unknown  |
|    f | unknown  |
|    g | unknown  |
|    h | unknown  |
|    i | unknown  |
|    j | unknown  |
|    k | rework   |
|    l | unknown  |
|    m | rework   |
|    n | unknown  |
|    o | verified |
|    p | unknown  |
|    q | unknown  |
|    r | rework   |
|    s | unknown  |
|    t | unknown  |
|    u | unknown  |
|    v | rework   |
|    w | unknown  |
|    x | unknown  |
|    y | unknown  |
|    z | unknown  |
|    A | unknown  |
|    B | unknown  |
|    C | unknown  |
|    D | unknown  |
|    E | unknown  |
|    F | unknown  |
|    G | unknown  |
|    H | unknown  |
|    I | unknown  |
|    J | unknown  |
|    K | unknown  |
|    L | unknown  |
|    M | unknown  |
|    N | unknown  |
|    O | unknown  |
|    P | unknown  |
|    Q | unknown  |
|    R | unknown  |
|    S | unknown  |
|    T | unknown  |
|    U | unknown  |
|    V | unknown  |
|    W | unknown  |
|    X | unknown  |
|    Y | unknown  |
|    Z | unknown  |
|    ! | verified |
|    " | verified |
|    # | unknown  |
|    $ | verified |
|    % | unknown  |
|    & | unknown  |
|    ' | verified |
|    ( | unknown  |
|    ) | unknown  |
|    * | unknown  |
|    + | unknown  |
|    , | unknown  |
|    - | verified |
|    . | verified |
|    / | unknown  |
|    : | verified |
|    ; | verified |
|    < | unknown  |
|    = | verified |
|    > | unknown  |
|    ? | unknown  |
|    @ | unknown  |
|    [ | unknown  |
|    \ | unknown  |
|    ] | unknown  |
|    ^ | unknown  |
|    _ | verified |
|    ` | unknown  |
|    { | unknown  |
|    \|| verified |
|    } | unknown  |
|    ~ | unknown  |
