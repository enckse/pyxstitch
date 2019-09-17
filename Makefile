TESTS        := $(shell find tests/ -type f -name "*.py" | sed "s!/!.!g;s!\.py!!g" | sort)
BIN          := bin
FORMAT       := pyxstitch
EXAMPLES     := examples/
SRC          := $(shell find tests/ -type f -name "*.py") setup.py $(shell find pyxstitch/ -type f -name "*.py")
PYPIRC       := $(shell echo $$HOME)/.pypirc
LANGS        := go c py ascii.txt
RUNS         := zoom fonts bash completions man
RUN_SH       := ./run.sh
PYPI         := pypi-test pypi-live
DEPS         := python3 python3-pil python3-pycodestyle python3-pydocstyle python3-pygments python3-setuptools git pydocstyle pycodestyle twine python3-docutils

all: test example analyze
example: clean ascii raw mapping symbols kvs banner logo $(RUNS)
languages: $(LANGS)

deps:
	apt-get install $(DEPS)

$(RUNS): clean
	$(RUN_SH) "$@"

$(LANGS):
	$(RUN_SH) "example" "$@"

banner:
	pyxstitch --version
	pyxstitch --version --quiet

ascii:
	$(RUN_SH) "example" "ascii.txt" "--theme bw" ".bw"
	$(RUN_SH) "ascii"
	cd $(EXAMPLES) && ./alphabet.sh

logo: 
	pyxstitch --file $(EXAMPLES)/logo.txt --quiet --multipage off --kv page_legend=1 --font monospace-ascii-3x7 --output $(BIN)/logo.png

pypi-check:
ifeq ($(wildcard $(PYPIRC)),)
		$(error missing pypirc file $(PYPIRC))
endif
	python3 setup.py sdist

$(PYPI): pypi-check
	./package.sh $@

raw:
	cd $(EXAMPLES) && ./replay.sh

mapping:
	$(RUN_SH) "bash" "--map 6c6c6c=ffffff --map 59c7b4=" ".map"

symbols:
	$(RUN_SH) "bash" "--symbols abcdef" ".symbol"

kvs:
	$(RUN_SH) "bash" "--kv page_height=700 page_width=900 page_pad=80 page_no_index=3 page_legend=2 page_font_size=10" ".cfg"
	$(RUN_SH) "bash" "--config tests/test.cfg" ".cfg"

text:
	cat $(EXAMPLES)test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	$(RUN_SH) "version" "$(BIN)/text.test.$(FORMAT)"
	diff -u $(BIN)/text.test.$(FORMAT) $(EXAMPLES)outputs/text.test.$(FORMAT)

analyze:
	pycodestyle $(SRC)
	pydocstyle $(SRC)

test: clean text
	python3 -m unittest $(TESTS)

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
	rm -rf dist/
