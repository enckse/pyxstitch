SRC=$(shell find . -type f -name "*.py" | grep -v "$(EXAMPLES)" | grep -v "build" | grep -v "bin")
TESTS=$(shell find tests/ -type f -name "*.py" | sed "s!/!.!g;s!\.py!!g")
VERS_PY=pyxstitch/version.py
BIN=bin
FORMAT=pyxstitch
TAG=$(shell git tag -l | sort -r | head -n 1 | sed "s/v//g" | sed "s/\./\\./g")
TAG_CURRENT=$(shell cat $(VERS_PY) | grep "$(TAG)")
EXAMPLES=examples/
EXAMPLE_OUT=$(EXAMPLES)outputs/
NO_TAG="na"
ifdef TRAVIS
TAG_CURRENT=$(NO_TAG)
endif
ifeq ($(TAG_CURRENT),)
TAG_CURRENT=$(NO_TAG)
endif
.PHONY:

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii raw bash fonts mapping symbols kvs banner logo

banner:
	pyxstitch --version
	pyxstitch --version --quiet

ascii:
	./run.sh "example" "ascii.txt"
	./run.sh "example" "ascii.txt" "--theme bw" ".bw"
	./run.sh "example" "ascii.txt" "--font monospace-ascii-3x7" ".3x7"
	./run.sh "example" "ascii.txt" "--font monospace-ascii-2x5" ".2x5"
	./run.sh "example" "ascii.txt" "--font monospace-ascii-3x5" ".3x5"
	./run.sh "example" "ascii.txt" "--font proportional-ascii-3x6" ".3x6"
	cd $(EXAMPLES) && ./alphabet.sh

fonts: clean
	./run.sh "fonts" "monospace" "5x9"
	./run.sh "fonts" "monospace" "3x7"
	./run.sh "fonts" "monospace" "2x5"
	./run.sh "fonts" "monospace" "3x5"
	./run.sh "fonts" "proportional" "3x6"

go:
	./run.sh "example" "go"

c:
	./run.sh "example" "c"

py:
	./run.sh "example" "py"

logo: 
	pyxstitch --file $(EXAMPLES)/logo.txt --quiet --multipage off --kv page_legend=1 --font monospace-ascii-3x7 --output $(BIN)/logo.png

raw:
	cd $(EXAMPLES) && ./replay.sh

bash:
	./run.sh "bash"

mapping:
	./run.sh "bash" "--map 6c6c6c=ffffff --map 59c7b4=" ".map"

symbols:
	./run.sh "bash" "--symbols abcdef" ".symbol"

kvs:
	./run.sh "bash" "--kv page_height=700 page_width=900 page_pad=80 page_no_index=3 page_legend=2 page_font_size=10" ".cfg"
	./run.sh "bash" "--config tests/test.cfg" ".cfg"

text:
	cat $(EXAMPLES)/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	./run.sh "version" "$(BIN)/text.test.$(FORMAT)"
	diff $(BIN)/text.test.$(FORMAT) $(EXAMPLE_OUT)text.test.$(FORMAT)

analyze:
	pip install pycodestyle pep257
	pycodestyle $(SRC)
	pep257 $(SRC)

version:
ifneq ($(TAG_CURRENT),$(NO_TAG))
	$(error version is not properly set)
endif

test: clean version text
	python -m unittest $(TESTS)

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
