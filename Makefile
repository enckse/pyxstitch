SRC=$(shell find . -type f -name "*.py" | grep -v "examples" | grep -v "build")
BIN=bin
HW="hello_world."
.PHONY:

run-example = pyxstitch --file examples/$(HW)$1 --output $(BIN)/$(HW)$1.png; \
			  diff $(BIN)/$(HW)$1.png examples/outputs/$(HW)$1.png

check: install test example analyze

install:
	python setup.py install

example: install clean go c py ascii

ascii:
	$(call run-example,"ascii.txt")

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

test: clean
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
