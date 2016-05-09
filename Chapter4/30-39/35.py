import parse

def get_nouns_from_sentence(sentence):
    result = []
    nouns = ''
    for i in range(0, len(sentence)):
        if sentence[i]['品詞'] == '名詞':
            nouns = nouns + sentence[i]['表層形']
        elif len(nouns) != 0:
            result.append(nouns)
            nouns = ''
    if len(nouns) != 0:
        result.append(nouns)
    return result

morpheme_data = parse.get_morpheme_from_neko()
print(parse.flatten(list(map(lambda sentence: get_nouns_from_sentence(sentence), morpheme_data))))
