import re

def remove_link(string):
    return re.sub(r'\[\[|\]\]', '', string)

