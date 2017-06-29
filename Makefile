SRC=$(shell find . -type f -name "*.py" | grep -v "examples")
BIN=bin
.PHONY:

analyze: test
	pep8 $(SRC)
	pep257 $(SRC)

test: clean
	cd tests && ./run.sh

clean:
	mkdir -p $(BIN)
	rm -f $(BIN)/*
