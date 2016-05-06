import re

article = open("../20/output.txt")
article_data = article.readlines()
article.close()

print(list(filter(lambda line: re.search(r'^\[\[Category:.+(\|\*)?\]\]$', line), article_data)))
