from functools import reduce
import re

_string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
_zipped = zip(range(1, len(_string.split(' '))), re.sub(r'[.,]', '', _string).split(' '))
print(reduce(lambda result, t: {**result, **{t[0]: (t[1][0:1] if t[0] in [1, 5, 6, 7, 8, 9, 15, 16, 19] else t[1][0:2])}}, _zipped, {}))
