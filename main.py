from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles
import pyxstitch.formatter as fmt

code = """
def main():
    print('Hello, World')

if __name__ == '__main__':
    main()"""
code = """
def aABCDEFG
    HIJK

LMNOPQRS

TUVWXYZ
AA AAAAAAAA BA AAWWWWA!
    AAAAAA
    W
"""

#code = ""
#import string
#for st in string.printable:
#    code += "st"
max_line = 0
lines = code.split("\n")
for line in lines:
    if len(line) > max_line:
        max_line = len(line)

spaced = []
for line in lines:
    padded = line
    while len(padded) < max_line:
        padded = padded + " "
    spaced.append(padded)

highlight(code, PythonLexer(), fmt.CrossStitchFormatter(style='monokai'))
