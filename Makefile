SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build" | grep -v "bin")
BIN=bin
FORMAT=raw
HW="hello_world."
.PHONY:

run-example = pyxstitch --file examples/$(HW)$1 --format $(FORMAT) --output $(BIN)/$(HW)$1.$(FORMAT); \
			  diff $(BIN)/$(HW)$1.$(FORMAT) examples/outputs/$(HW)$1.$(FORMAT)

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii

ascii:
	$(call run-example,"ascii.txt")
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

analyze:
	pip install pep8 pep257
	pep8 $(SRC)
	pep257 $(SRC)

unverified: install clean
	$(shell cat README.md | grep "^|    " | grep -v "verified" | sed "s/|    //g;s/ | .*//g" | tr '\n' ' '| sed 's/ //g' | sed "s/'/\'/g" > $(BIN)/unverified.py)
	pyxstitch --file $(BIN)/unverified.py --output $(BIN)/unverified.png

test: clean
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
