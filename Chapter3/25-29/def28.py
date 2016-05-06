import re

def remove_other(string):
    return remove_ref(string)

def remove_ref(string):
    return re.sub(r'<ref.*?>|</ref>', '', string)
