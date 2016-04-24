import n_gram

STRING_X = 'paraparaparadise'
STRING_Y = 'paragraph'

x = n_gram.create(STRING_X, 2)
y = n_gram.create(STRING_Y, 2)

print('x: ', x)
print('y: ', y)
print('union: ', set(x) & set(y))
print('intersection: ', set(x) | set(y))
print('difference(x - y): ', set(x) - set(y))
print('difference(y - x): ', set(y) - set(x))
print("x has 'se': ", 'se' in x)
print("y has 'se': ", 'se' in y)
