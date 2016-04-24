from functools import reduce
import re

_string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print(list(map(lambda word: len(word), re.sub(r'[.,]', '', _string).split(' '))))
