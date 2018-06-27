TESTS        := $(shell find tests/ -type f -name "*.py" | sed "s!/!.!g;s!\.py!!g" | sort)
BIN          := bin
FORMAT       := pyxstitch
EXAMPLES     := examples/
EXAMPLE_OUT  := $(EXAMPLES)outputs/
SRC          := $(shell find . -type f -name "*.py" | grep -v "$(EXAMPLES)" | grep -v "build" | grep -v "bin")
PYPIRC       := $(shell echo $$HOME)/.pypirc
APPVEYOR     := appveyor.yml
TMP_APPVEYOR := $(BIN)/$(APPVEYOR)
LANGS        := go c py ascii.txt
RUNS         := zoom fonts bash completions man
INSTALL      :=
INSTALL_OPTS := --root="$(INSTALL)/" --optimize=1
RUN_SH       := ./run.sh
PACK_SH      := ./package.sh
PYPI         := pypi-test pypi-live

# groupings
all: install check
check: test example appveyor analyze
example: install clean ascii raw mapping symbols kvs banner logo runs

# meta
runs: $(RUNS)
languages: $(LANGS)

install:
	python setup.py install $(INSTALL_OPTS)

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
	pip install twine docutils
ifeq ($(wildcard $(PYPIRC)),)
		$(error missing pypirc file $(PYPIRC))
endif
	python setup.py sdist

$(PYPI): pypi-check
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
	cat $(EXAMPLES)/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	$(RUN_SH) "version" "$(BIN)/text.test.$(FORMAT)"
	diff -u $(BIN)/text.test.$(FORMAT) $(EXAMPLE_OUT)text.test.$(FORMAT)

analyze:
	pycodestyle $(SRC)
	pep257 $(SRC)

test: clean text
	python -m unittest $(TESTS)

appveyor: clean
	cat $(APPVEYOR) | head -n -2 > $(TMP_APPVEYOR)
	@echo "test_script:" >> $(TMP_APPVEYOR)
	@echo "  - python -m unittest $(TESTS)" >> $(TMP_APPVEYOR)
	cat $(TMP_APPVEYOR) > $(APPVEYOR)

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
	rm -rf dist/
