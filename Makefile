SRC=$(shell find . -type f -name "*.py" | grep -v "$(EXAMPLES)" | grep -v "build" | grep -v "bin")
VERS_PY=pyxstitch/version.py
VERS=$(shell cat $(VERS_PY) | grep "__version__" | cut -d "=" -f 2 | sed "s/ //g")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
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

handle-version = sed -i "s/$(VERS)/__VERSION__/g" $1

run-example = pyxstitch --file $(EXAMPLES)/$(HW)$1 --multipage off --format $(FORMAT) --output $(BIN)/$(HW)$1.$(FORMAT) $2 $4 $5 $6; \
			  pyxstitch --file $(BIN)/$(HW)$1.$(FORMAT) --output $(BIN)/$(HW)$1.png $2; \
			  $(call handle-version,$(BIN)/$(HW)$1.$(FORMAT)); \
			  diff $(BIN)/$(HW)$1.$(FORMAT) $(EXAMPLE_OUT)$(HW)$1.$(FORMAT)$3;

gen-font = pyxstitch --file $(EXAMPLES)/$(HW)"ascii.txt" --theme bw --kv page_legend=1 --multipage off --output $(BIN)/$1.png --font $1-ascii-$2;

run-bash = pyxstitch --file $(EXAMPLES)/fizzbuzz.bash --multipage off --font monospace-ascii-5x9 --format $(FORMAT) --output $(BIN)/fb.bash.$(FORMAT) $1;  \
			  $(call handle-version,$(BIN)/fb.bash.$(FORMAT)); \
			  diff $(BIN)/fb.bash.$(FORMAT) $(EXAMPLE_OUT)fb.bash.$(FORMAT)$2;

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii raw bash fonts mapping symbols kvs

ascii:
	$(call run-example,"ascii.txt")
	$(call run-example,"ascii.txt",--theme bw,".bw")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x7,".3x7")
	$(call run-example,"ascii.txt",--font monospace-ascii-2x5,".2x5")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x5,".3x5")
	$(call run-example,"ascii.txt",--font proportional-ascii-3x6,".3x6")
	cd $(EXAMPLES) && ./alphabet.sh

fonts: clean
	$(call gen-font,"monospace","5x9")
	$(call gen-font,"monospace","3x7")
	$(call gen-font,"monospace","2x5")
	$(call gen-font,"monospace","3x5")
	$(call gen-font,"proportional","3x6")

go:
	$(call run-example,"go",,)

c:
	$(call run-example,"c",,)

py:
	$(call run-example,"py",,)

logo: install
	pyxstitch --file $(EXAMPLES)/logo.txt --multipage off --kv page_legend=1 --font monospace-ascii-3x7 --output images/logo.png

raw:
	cd $(EXAMPLES) && ./replay.sh

bash:
	$(call run-bash,,)

mapping:
	$(call run-bash,--map 6c6c6c=ffffff --map 59c7b4=,".map")

symbols:
	$(call run-bash,--symbols "abcdef",".symbol")

kvs:
	$(call run-bash,--kv page_height=700 page_width=900 page_pad=80 page_no_index=3 page_legend=2 page_font_size=10,".cfg")
	$(call run-bash,--config tests/test.cfg,".cfg")

text:
	cat $(EXAMPLES)/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	$(call handle-version,$(BIN)/text.test.$(FORMAT))
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
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
