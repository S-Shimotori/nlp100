import parse
from functools import reduce
import numpy
import matplotlib.pyplot
from collections import Counter

morpheme_data = parse.get_morpheme_from_neko()

counter_by_word= parse.get_counter_from_words(parse.flatten(morpheme_data)).items()
counter_by_number = list(Counter(list(map(lambda count: count[1], counter_by_word))).items())
sorted_by_number = sorted(counter_by_number, key = lambda value: value[0])
x = numpy.array(reduce(lambda result, count: result + [count[0]], sorted_by_number, []))
y = numpy.array(reduce(lambda result, count: result + [count[1]], sorted_by_number, []))
matplotlib.pyplot.bar(x, y, align = 'center')
matplotlib.pyplot.show()
