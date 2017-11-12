# -*- encoding=utf-8 -*-
from __future__ import print_function
from utf8fixer import fix_encoding

contents = [
    u"árbol, miré, sí, canción, único, pingüino, niña",
    u"ĂĄrbol, mirĂŠ, sĂ­, canciĂłn, Ăşnico, pingĂźino, niĂąa"
]

print("\nFixed but not normalized:")
for i, content in enumerate(contents):
    # fix_encoding(content, encoding="latin2")
    contents[i] = fix_encoding(content)
    print(contents[i])

print("\nFixed and normalized:")
for i, content in enumerate(contents):
    # fix_encoding(content, encoding="latin2", norm=True)
    contents[i] = fix_encoding(content, norm=True)
    print(contents[i])


# output:
# Fixed but not normalized:
# árbol, miré, sí, canción, único, pingüino, niña
# árbol, miré, sí, canción, único, pingüino, niña

# Fixed and normalized:
# arbol, mire, si, cancion, unico, pinguino, nina
# arbol, mire, si, cancion, unico, pinguino, nina
