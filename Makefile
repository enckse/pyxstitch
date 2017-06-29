SRC=$(shell find . -type f -name "*.py" | grep -v "examples")
BIN=bin
.PHONY:

check: test example analyze

example: clean
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
