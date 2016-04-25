from more_itertools import chunked
from functools import reduce
import sys
import string
import itertools

N = int(sys.argv[1])
hightemp = open('../hightemp.txt')
hightemp_data = hightemp.readlines()
hightemp.close()

chunked_data = list(chunked(hightemp_data, N))
lowercases = list(string.ascii_lowercase)
keys = list(map(lambda tup: ''.join(tup), itertools.product(lowercases, lowercases)))[:len(chunked_data)]
for element in zip(keys, chunked_data):
    output = open('output_python/output_' + element[0], 'w')
    output.write(''.join(element[1]))
    output.close()
