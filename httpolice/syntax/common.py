# -*- coding: utf-8; -*-

from httpolice.parse import (
    char_class,
    char_range,
    literal,
    maybe,
    string1,
    wrap,
)


# RFC 5234

ALPHA = char_range(0x41, 0x5A) + char_range(0x61, 0x7A)
alpha = char_class(ALPHA)
crlf = (~maybe('\r') + '\n')   // u'newline'
DIGIT = char_range(0x30, 0x39)
digit = char_class(DIGIT)
HEXDIG = DIGIT + 'ABCDEFabcdef'
hexdig = char_class(HEXDIG)
HTAB = '\t'
SP = ' '
sp = literal(SP)
sp_htab = char_class(SP + HTAB)
VCHAR = char_range(0x21, 0x7E)
DQUOTE = '"'
dquote = literal(DQUOTE)


# Auxiliary

integer = wrap(int, string1(digit))
hex_integer = wrap(lambda s: int(s, 16), string1(hexdig))
