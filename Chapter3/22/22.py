from functools import reduce
import re

article = open("../20/output.txt")
article_data = article.readlines()
article = article.close()

def is_category(string):
    return True if re.search(r'(?<=\[\[Category:).*?(?=\]\])', string) else False

def get_category_name(string):
    return re.search(r"(?<=\[\[Category:).*?(?=(\|\*)?\]\])", string).group(0)

print(list(map(lambda line: get_category_name(line), list(filter(lambda line: is_category(line), article_data)))))
