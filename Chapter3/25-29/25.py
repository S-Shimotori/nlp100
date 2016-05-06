from functools import reduce
import re
import def26
import def27
import def28
import def29

article = open('../20/output.txt')
article_data = article.readlines()
article.close()

counter = 0
for line in article_data:
    counter += 1
    if line == "{{基礎情報 国\n":
        break
information = []
for line in article_data[counter:]:
    if line != "}}\n":
        if line.startswith('|'):
            information.append(line)
        else:
            information[-1] += line
    else:
        break

def remove_markup(string):
    return def28.remove_other(def27.remove_link(def26.remove_bold(string)))

information_dict = dict(reduce(lambda result, data: {**result, **{data[0]: remove_markup(data[1])}}, list(map(lambda data: re.match(r'\|(.*) = ([\s\S]*)', data).groups(), information)), {}))
print(information_dict)

print(def29.get_flag_image_url(information_dict))
