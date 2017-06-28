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

highlight(code, PythonLexer(), fmt.CrossStitchFormatter(style='monokai'))
