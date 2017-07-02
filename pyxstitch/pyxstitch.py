#!/usr/bin/python
"""App for pyxstitch."""
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.styles import get_all_styles
import pyxstitch.formatter as fmt
import pyxstitch.output as out_fmt
import argparse
import os
import sys


def main():
    """Main-entry point."""
    _PNG = "png"
    _RAW = out_fmt.RAW_FORMAT
    parser = argparse.ArgumentParser(
            description='Convert source code files to cross stitch patterns.')
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--output', type=str)
    parser.add_argument('--colorize', action='store_true')
    parser.add_argument('--dark', action='store_true')
    parser.add_argument('--format', type=str, default=_PNG,
                        choices=[_PNG, "pdf", "jpg", _RAW])
    parser.add_argument('--style',
                        default='monokai',
                        choices=list(get_all_styles()))
    args = parser.parse_args()
    lexer = get_lexer_for_filename(args.file)
    content = None
    file_name = None
    if os.path.exists(args.file):
        file_name = os.path.splitext(args.file)[0]
        with open(args.file, 'r') as f:
            content = f.read()
    else:
        file_name = "output"
        content = "".join(sys.stdin.readlines())
    formatting = fmt.CrossStitchFormatter(style=args.style)
    formatting.colorize = args.colorize
    formatting.dark = args.dark
    formatting.file_name = args.output
    formatting.is_raw = args.format == _RAW
    text = formatting.preprocess(content)
    if args.output is None:
        formatting.file_name = "{}.{}".format(file_name, args.format)
    highlight(text, lexer, formatting)

if __name__ == '__main__':
    main()
