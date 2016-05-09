import parse

def is_verb(word):
    return word['品詞'] == '動詞'

morpheme_data = parse.get_morpheme_from_neko()
print(list(map(lambda morpheme: morpheme['原形'], parse.get_word_with_parameter(morpheme_data, is_verb))))
