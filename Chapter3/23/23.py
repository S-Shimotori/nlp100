from functools import reduce
import re

article = open('../20/output.txt')
article_data = article.readlines()
article.close()

def get_section(string):
    if re.match(r'^=+[^=]*=+$', string):
        length_tuple = re.match(r'^(=+)(.*?)(=+)$', string).group(1, 2, 3)
        return [(len(length_tuple[0]) - 1, length_tuple[1])] if len(length_tuple[0]) == len(length_tuple[2]) else []
    else:
        return []

print(list(reduce(lambda result, line: result + get_section(line) , article_data, [])))
