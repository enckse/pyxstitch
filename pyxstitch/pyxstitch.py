#!/usr/bin/python
"""App for pyxstitch."""
from pygments import highlight
from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.styles import get_all_styles
import pyxstitch.formatter as fmt
import pyxstitch.output as out_fmt
import argparse
import os
import sys

_PNG = "png"
_RAW = out_fmt.RAW_FORMAT
_DEF_STYLE = "monokai"
_PDF = "pdf"
_TXT = ".txt"


def _create_file_name(file_name, args):
    """Create output file names."""
    return "{}.{}".format(file_name, args.format)


def _replay(args, file_name, content):
    """Do replay."""
    if args.format == _RAW:
        print("can not replay raw to raw")
        exit(1)
    if args.colorize or args.dark or args.style != _DEF_STYLE:
        print('style, colorize, and dark ignored during replay')
    out = args.output
    if args.output is None:
        out = _create_file_name(file_name, args)
    playback = out_fmt.TextFormat()
    playback.replay(content, out)
    exit(0)


def main():
    """Main-entry point."""
    parser = argparse.ArgumentParser(
            description='Convert source code files to cross stitch patterns.')
    parser.add_argument('--file', type=str, default=_TXT)
    parser.add_argument('--guess', action='store_true')
    parser.add_argument('--output', type=str)
    parser.add_argument('--colorize', action='store_true')
    parser.add_argument('--dark', action='store_true')
    parser.add_argument('--kv', metavar='N', type=str, nargs='+')
    parser.add_argument('--multipage', type=str,
                        default=out_fmt.MULTI_PAGE_AUTO,
                        choices=[out_fmt.MULTI_PAGE_AUTO,
                                 out_fmt.MULTI_PAGE_ON,
                                 out_fmt.MULTI_PAGE_OFF])
    parser.add_argument('--format', type=str, default=_PNG,
                        choices=[_PNG, _PDF, "jpg", _RAW])
    parser.add_argument('--style',
                        default=_DEF_STYLE,
                        choices=list(get_all_styles()))
    args = parser.parse_args()
    content = None
    file_name = None
    file_ext = os.path.splitext(args.file)
    is_raw = False
    for item in file_ext:
        if item == "." + _RAW:
            is_raw = True
            break
    if not is_raw:
        lexer = get_lexer_for_filename(args.file)
    if os.path.exists(args.file):
        file_name = file_ext[0]
        with open(args.file, 'r') as f:
            content = f.read()
        if is_raw:
            _replay(args, file_name, content)
    else:
        if file_ext[1] is not None and len(file_ext[1]) > 1:
            print("file not found, pass extension for stdin or valid file")
            exit(1)
        file_name = "output"
        content = "".join(sys.stdin.readlines())
        if is_raw:
            _replay(args, file_name, content)
        if args.guess:
            try:
                lexer = guess_lexer(content)
                print('using {} lexer'.format(lexer.name))
            except:
                print('unable to guess a lexer...defaulting to text')
                lexer = get_lexer_for_filename(_TXT)
    formatting = fmt.CrossStitchFormatter(style=args.style)
    formatting.colorize = args.colorize
    formatting.dark = args.dark
    formatting.file_name = args.output
    formatting.is_multipage = args.multipage
    formatting.is_raw = args.format == _RAW
    if args.kv is not None and len(args.kv) > 0:
        formatting.config = args.kv
    text = formatting.preprocess(content)
    if args.output is None:
        formatting.file_name = _create_file_name(file_name, args)
    highlight(text, lexer, formatting)

if __name__ == '__main__':
    main()
