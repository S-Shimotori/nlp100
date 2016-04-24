import n_gram

_string = 'I am an NLPer'
_n = 2

print(n_gram.create(_string.split(' '), _n))
print(n_gram.create(_string, _n))
