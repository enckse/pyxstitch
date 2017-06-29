SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build")
BIN=bin
.PHONY:

check: install test example analyze

install:
	python setup.py install

example: install clean
	go build -o $(BIN)/go_hw examples/hello_world.go
	gcc examples/hello_world.c -o $(BIN)/c_hw
	python examples/hello_world.py &>/dev/null
	cd examples && ./run.sh

analyze:
	pep8 $(SRC)
	pep257 $(SRC)

test: clean
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
