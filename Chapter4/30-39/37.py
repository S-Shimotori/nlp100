import parse
from functools import reduce
import numpy
import matplotlib.pyplot

morpheme_data = parse.get_morpheme_from_neko()

counter = parse.get_counter_from_words(parse.flatten(morpheme_data)).most_common(10)

xticks = numpy.array(reduce(lambda result, count: result + [count[0][0]], counter, []))
x = numpy.array(list(range(1, 11)))
y = numpy.array(reduce(lambda result, count: result + [count[1]], counter, []))
matplotlib.pyplot.bar(x, y, align = 'center')
matplotlib.pyplot.xticks(x, xticks)
matplotlib.pyplot.show()
