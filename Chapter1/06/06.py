import n_gram

_string0 = 'paraparaparadise'
_string1 = 'paragraph'

x = n_gram.create(_string0, 2)
y = n_gram.create(_string1, 2)

print('x: ', x)
print('y: ', y)
print('union: ', set(x) & set(y))
print('intersection: ', set(x) | set(y))
print('difference(x - y): ', set(x) - set(y))
print('difference(y - x): ', set(y) - set(x))
print("x has 'se': ", 'se' in x)
print("y has 'se': ", 'se' in y)
