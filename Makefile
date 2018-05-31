SRC=$(shell find . -type f -name "*.py" | grep -v "$(EXAMPLES)" | grep -v "build" | grep -v "bin")
TESTS=$(shell find tests/ -type f -name "*.py" | sed "s!/!.!g;s!\.py!!g")
BIN=bin
MAN1=pyxstitch.1
FORMAT=pyxstitch
EXAMPLES=examples/
EXAMPLE_OUT=$(EXAMPLES)outputs/
PYPIRC=$(shell echo $$HOME)/.pypirc
APPVEYOR=appveyor.yml
TMP_APPVEYOR=$(BIN)/$(APPVEYOR)
INSTALL :=

check: install test example appveyor completion analyze

install:
	python setup.py install --root="$(INSTALL)/" --optimize=1

example: install clean go c py ascii raw bash fonts mapping symbols zoom kvs banner logo

zoom:
	./run.sh "zoom"

banner:
	pyxstitch --version
	pyxstitch --version --quiet

ascii:
	./run.sh "example" "ascii.txt"
	./run.sh "example" "ascii.txt" "--theme bw" ".bw"
	./run.sh "ascii"
	cd $(EXAMPLES) && ./alphabet.sh

fonts: clean
	./run.sh "fonts"

go:
	./run.sh "example" "go"

c:
	./run.sh "example" "c"

py:
	./run.sh "example" "py"

logo: 
	pyxstitch --file $(EXAMPLES)/logo.txt --quiet --multipage off --kv page_legend=1 --font monospace-ascii-3x7 --output $(BIN)/logo.png

pypi-check:
	pip install twine docutils
ifeq ($(wildcard $(PYPIRC)),)
		$(error missing pypirc file $(PYPIRC))
endif
	python setup.py sdist

pypi-test: pypi-check
	./package.sh test

pypi-live: pypi-check
	./package.sh

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

test: clean text
	python -m unittest $(TESTS)

appveyor: clean
	cat $(APPVEYOR) | head -n -2 > $(TMP_APPVEYOR)
	@echo "test_script:" >> $(TMP_APPVEYOR)
	@echo "  - python -m unittest $(TESTS)" >> $(TMP_APPVEYOR)
	mv $(TMP_APPVEYOR) $(APPVEYOR)

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
	rm -rf dist/

completion:
	./run.sh "completions"

man: clean
	./run.sh "man"
