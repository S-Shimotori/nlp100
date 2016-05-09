import parse
from functools import reduce
import numpy
import matplotlib.pyplot

morpheme_data = parse.get_morpheme_from_neko()

counter_by_word = list(parse.get_counter_from_words(parse.flatten(morpheme_data)).items())
sorted_by_number = sorted(list(map(lambda count: count[1], counter_by_word)), reverse = True)
matplotlib.pyplot.plot(sorted_by_number)
matplotlib.pyplot.xscale('log')
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.show()
