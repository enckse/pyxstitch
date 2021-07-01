TESTS        := $(shell find tests/ -type f -name "*.py" | sed "s!/!.!g;s!\.py!!g" | sort)
BIN          := bin
FORMAT       := pyxstitch
EXAMPLES     := examples/
SRC          := $(shell find tests/ -type f -name "*.py") setup.py $(shell find pyxstitch/ -type f -name "*.py")
PYPIRC       := $(shell echo $$HOME)/.pypirc
LANGS        := go c py ascii.txt
RUNS         := srcver zoom fonts bash completions man
RUN_SH       := ./resources/build.sh
PACK_SH      := ./resources/package.sh
PYPI         := pypi-test pypi-live
PYTHON_BIN   := python3

export PYTHON_BIN

all: test example analyze
example: clean ascii raw mapping symbols kvs banner logo $(RUNS)
languages: $(LANGS)

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
	$(PYTHON_BIN) setup.py sdist

$(PYPI): pypi-check
	$(PYTHON_BIN) -c "import docutils; import twine"
	$(PACK_SH) $@

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
	flake8 $(SRC)

test: clean text
	$(PYTHON_BIN) -m unittest $(TESTS)

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*

integration:
	$(PYTHON_BIN) -c "import pygments; import PIL; import setuptools"
	pycodestyle --version
	pydocstyle --version
	flake8 --version
	$(PYTHON_BIN) setup.py install
	rm -rf dist/ build/ pyxstitch/pyxstitch.egg-info/
