import re

def remove_bold(string):
    return re.sub(r"'{2}|'{3}|'{5}", '', string)
