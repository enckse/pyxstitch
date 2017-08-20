SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build" | grep -v "bin")
BIN=bin
FORMAT=pyxstitch
HW="hello_world."
.PHONY:

run-example = pyxstitch --file examples/$(HW)$1 --multipage off --format $(FORMAT) --output $(BIN)/$(HW)$1.$(FORMAT) $2; \
			  pyxstitch --file $(BIN)/$(HW)$1.$(FORMAT) --output $(BIN)/$(HW)$1.png $2; \
			  diff $(BIN)/$(HW)$1.$(FORMAT) examples/outputs/$(HW)$1.$(FORMAT);

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii raw bash

ascii:
	$(call run-example,"ascii.txt")
	$(call run-example,"ascii.txt",--font ThreeBySeven)
	cd examples && ./alphabet.sh

go:
	go build -o $(BIN)/go_hw examples/hello_world.go
	$(call run-example,"go")

c:
	gcc examples/hello_world.c -o $(BIN)/c_hw
	$(call run-example,"c")

py:
	python examples/hello_world.py &>/dev/null
	$(call run-example,"py")

raw:
	pyxstitch --file examples/hw.py.pyxstitch --output $(BIN)/hw.py.png

bash:
	pyxstitch --file examples/fizzbuzz.bash --multipage off --format $(FORMAT) --output $(BIN)/fb.bash.$(FORMAT)
	diff $(BIN)/fb.bash.$(FORMAT) examples/outputs/fb.bash.$(FORMAT)

text:
	cat tests/test.txt | pyxstitch --format $(FORMAT) --output $(BIN)/text.test.$(FORMAT) --multipage off
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
