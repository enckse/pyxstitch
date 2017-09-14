SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build" | grep -v "bin")
VERS_PY=pyxstitch/version.py
VERS=$(shell cat $(VERS_PY) | grep "__version__" | cut -d "=" -f 2 | sed "s/ //g")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
TAG=$(shell git tag -l | sort -r | head -n 1 | sed "s/v//g" | sed "s/\./\\./g")
TAG_CURRENT=$(shell cat $(VERS_PY) | grep "$(TAG)")
EXAMPLES=examples/outputs/
NO_TAG="na"
ifdef TRAVIS
TAG_CURRENT=$(NO_TAG)
endif
ifeq ($(TAG_CURRENT),)
TAG_CURRENT=$(NO_TAG)
endif
.PHONY:

handle-version = sed -i "s/$(VERS)/__VERSION__/g" $1

run-example = pyxstitch --file examples/$(HW)$1 --multipage off --format $(FORMAT) --output $(BIN)/$(HW)$1.$(FORMAT) $2 $4 $5 $6; \
			  pyxstitch --file $(BIN)/$(HW)$1.$(FORMAT) --output $(BIN)/$(HW)$1.png $2; \
			  $(call handle-version,$(BIN)/$(HW)$1.$(FORMAT)); \
			  diff $(BIN)/$(HW)$1.$(FORMAT) $(EXAMPLES)$(HW)$1.$(FORMAT)$3;

gen-font = pyxstitch --file examples/$(HW)"ascii.txt" --theme bw --kv page_legend=1 --multipage off --output $(BIN)/$1.png --font monospace-ascii-$1;

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii raw bash fonts  mapping

ascii:
	$(call run-example,"ascii.txt")
	$(call run-example,"ascii.txt",--theme bw,".bw")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x7,".3x7")
	$(call run-example,"ascii.txt",--font monospace-ascii-2x5,".2x5")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x5,".3x5")
	cd examples && ./alphabet.sh

fonts: clean
	$(call gen-font,"5x9")
	$(call gen-font,"3x7")
	$(call gen-font,"2x5")
	$(call gen-font,"3x5")

go:
	$(call run-example,"go",,,--command,"go build -o $(BIN)/go_hw examples/hello_world.go",--shell)

c:
	$(call run-example,"c",,,--command,"gcc examples/hello_world.c -o $(BIN)/c_hw",--shell)

py:
	$(call run-example,"py",,,--command,"python examples/hello_world.py",--shell)

logo: install
	pyxstitch --file examples/logo.txt --multipage off --kv page_legend=1 --font monospace-ascii-3x7 --output images/logo.png

raw:
	cd examples && ./replay.sh

bash:
	pyxstitch --file examples/fizzbuzz.bash --multipage off --font monospace-ascii-5x9 --format $(FORMAT) --output $(BIN)/fb.bash.$(FORMAT)
	$(call handle-version,$(BIN)/fb.bash.$(FORMAT))
	diff $(BIN)/fb.bash.$(FORMAT) $(EXAMPLES)fb.bash.$(FORMAT)

mapping:
	pyxstitch --file examples/fizzbuzz.bash --multipage off --font monospace-ascii-5x9 --format $(FORMAT) --output $(BIN)/fb.bash.$(FORMAT)  --map 6c6c6c=ffffff --map 59c7b4=
	$(call handle-version,$(BIN)/fb.bash.$(FORMAT))
	diff $(BIN)/fb.bash.$(FORMAT) $(EXAMPLES)fb.bash.$(FORMAT).map

text:
	cat examples/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	$(call handle-version,$(BIN)/text.test.$(FORMAT))
	diff $(BIN)/text.test.$(FORMAT) $(EXAMPLES)text.test.$(FORMAT)

analyze:
	pip install pep8 pep257
	pep8 $(SRC)
	pep257 $(SRC)

version:
ifneq ($(TAG_CURRENT),$(NO_TAG))
	$(error version is not properly set)
endif

test: clean version text
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
