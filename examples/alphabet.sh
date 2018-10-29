#!/bin/bash
file_names=".alphabet.py"
python3 -c "import string

def write_file(name, sets):
    with open('../bin/' + name + '$file_names', 'w') as f:
        f.write(''.join(sets))

lowers = [x for x in string.printable if x >= 'a' and x <= 'z']
nums = [x for x in string.printable if x >= '0' and x <= '9']
uppers = [x for x in string.printable if x >= 'A' and x <= 'Z']
others = [x for x in string.printable if x not in lowers + uppers + nums and len(x.strip()) != 0]
write_file('lower', lowers)
write_file('upper', uppers)
write_file('nums', nums)
write_file('other', others)
"
if [ $? -ne 0 ]; then
    echo "unable to generate alphabet..."
    exit 1
fi
for a in $(find ../bin/ -name "*$file_names"); do
    pyxstitch --file $a --output outputs/$(basename $a | sed "s/$file_names/.png/g")
    if [ $? -ne 0 ]; then
        echo "problem with $a"
        exit 1
    fi
done
