SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build" | grep -v "bin")
VERS=$(shell cat pyxstitch/version.py | grep "__version__" | cut -d "=" -f 2 | sed "s/ //g")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
.PHONY:

handle-version = sed -i "s/$(VERS)/__VERSION__/g" $1

run-example = pyxstitch --file examples/$(HW)$1 --multipage off --format $(FORMAT) --output $(BIN)/$(HW)$1.$(FORMAT) $2 $4 $5 $6; \
			  pyxstitch --file $(BIN)/$(HW)$1.$(FORMAT) --output $(BIN)/$(HW)$1.png $2; \
			  $(call handle-version,$(BIN)/$(HW)$1.$(FORMAT)); \
			  diff $(BIN)/$(HW)$1.$(FORMAT) examples/outputs/$(HW)$1.$(FORMAT)$3;

gen-font = pyxstitch --file examples/$(HW)"ascii.txt" --theme bw --kv page_legend=1 --multipage off --output $(BIN)/$1.png --font monospace-ascii-$1;

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii raw bash fonts

ascii:
	$(call run-example,"ascii.txt")
	$(call run-example,"ascii.txt",--theme bw,".bw")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x7,".3x7")
	$(call run-example,"ascii.txt",--font monospace-ascii-2x5,".2x5")
	$(call run-example,"ascii.txt",--font monospace-ascii-3x5,".3x5")
	cd examples && ./alphabet.sh

fonts:
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
	pyxstitch --file examples/hw.py.pyxstitch --output $(BIN)/hw.py.png

bash:
	pyxstitch --file examples/fizzbuzz.bash --multipage off --format $(FORMAT) --output $(BIN)/fb.bash.$(FORMAT)
	$(call handle-version,$(BIN)/fb.bash.$(FORMAT))
	diff $(BIN)/fb.bash.$(FORMAT) examples/outputs/fb.bash.$(FORMAT)

text:
	cat tests/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
	$(call handle-version,$(BIN)/text.test.$(FORMAT))
	diff $(BIN)/text.test.$(FORMAT) tests/text.test.$(FORMAT)

analyze:
	pip install pep8 pep257
	pep8 $(SRC)
	pep257 $(SRC)

test: clean text
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
