import random

_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(' '.join(list(map(lambda word: word[:1] + ''.join(random.sample(list(word[1:-1]), len(word) - 2)) + word[-1:] if len(word) > 4 else word, _string.split(' ')))))

