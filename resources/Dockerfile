FROM debian:unstable

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 git flake8 pydocstyle pycodestyle build-essential python3-pygments python3-pil sudo
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 100
RUN mkdir /workdir
WORKDIR /workdir
RUN git clone git://cgit.voidedtech.com/pyxstitch

WORKDIR /workdir/pyxstitch
RUN make check
