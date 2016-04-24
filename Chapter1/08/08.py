from functools import reduce
import re

_string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

def cipher(string):
    return ''.join(list(map(lambda c: chr(219 - ord(c)) if re.search(r'[a-z]', c) else c, string)))

encoded = cipher(_string)
decoded = cipher(encoded)
print(_string)
print(encoded)
print(decoded)
