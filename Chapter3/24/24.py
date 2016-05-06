from functools import reduce
import re

article = open('../20/output.txt')
article_data = article.readlines()
article.close()

pattern = r'(\[\[|^)(ファイル|File):([^|]+)'
print(list(map(lambda line: re.search(pattern, line).group(3), list(filter(lambda line: re.search(pattern, line), article_data)))))

