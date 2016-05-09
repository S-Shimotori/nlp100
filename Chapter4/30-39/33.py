import parse

def is_noun_by_suru(word):
    return word['品詞'] == '名詞' and word['品詞細分類1'] == 'サ変接続'

morpheme_data = parse.get_morpheme_from_neko()
print(list(map(lambda morpheme: morpheme['表層形'], parse.get_word_with_parameter(morpheme_data, is_noun_by_suru))))
