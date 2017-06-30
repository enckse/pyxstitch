#!/usr/bin/python
"""App for pyxstitch."""
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.styles import get_all_styles
import pyxstitch.formatter as fmt
import argparse
import os


def main():
    """Main-entry point."""
    _PNG = "png"
    _RAW = "raw"
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
    with open(args.file, 'r') as f:
        formatting = fmt.CrossStitchFormatter(style=args.style)
        formatting.colorize = args.colorize
        formatting.dark = args.dark
        formatting.file_name = args.output
        formatting.is_raw = args.format == _RAW
        text = formatting.preprocess(f.read())
        if args.output is None:
            parts = os.path.splitext(args.file)
            formatting.file_name = "{}.{}".format(parts[0], args.format)
        highlight(text, lexer, formatting)

if __name__ == '__main__':
    main()
