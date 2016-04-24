import n_gram

STRING = 'I am an NLPer'
N = 2

print(n_gram.create(STRING.split(' '), N))
print(n_gram.create(STRING, N))
