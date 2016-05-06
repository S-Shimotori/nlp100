import json
import gzip

jawiki_country = gzip.open("../jawiki-country.json.gz", 'r')
jawiki_country_data = jawiki_country.readlines()
jawiki_country.close()

for line in jawiki_country_data:
    article = json.loads(line.decode("utf-8"))
    if article['title'] == 'イギリス':
        output = open('output.txt', 'w')
        output.write(article['text'])
        output.close()
        break
