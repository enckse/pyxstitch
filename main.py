#!/usr/bin/python
"""App for pyxstitch."""
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.styles import get_all_styles
import pyxstitch.formatter as fmt
import argparse


def main():
    """Main-entry point."""
    parser = argparse.ArgumentParser(
            description='Convert source code files to cross stitch patterns.')
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--colorize', action='store_true')
    parser.add_argument('--style', default='monokai', choices=get_all_styles())
    args = parser.parse_args()
    lexer = get_lexer_for_filename(args.file)
    with open(args.file, 'r') as f:
        formatting = fmt.CrossStitchFormatter(style=args.style)
        formatting.colorize = args.colorize
        highlight(f.read(), lexer, formatting)

if __name__ == '__main__':
    main()
