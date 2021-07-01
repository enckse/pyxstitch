FROM alpine:3.14

RUN apk add --no-cache python3 git py3-pillow py3-pygments py3-pycodestyle py3-pydocstyle py3-flake8 sudo make py3-setuptools bash
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN mkdir /workdir
WORKDIR /workdir
RUN git clone git://cgit.voidedtech.com/pyxstitch

WORKDIR /workdir/pyxstitch
RUN make check
