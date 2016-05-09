import parse

def get_noun_phrase_from_sentence(sentence):
    result = []
    for i in range(1, len(sentence) - 1):
        word = sentence[i]
        if word['表層形'] == 'の' and word['品詞'] == '助詞' and word['品詞細分類1'] == '連体化' and sentence[i - 1]['品詞'] == '名詞' and sentence[i + 1]['品詞'] == '名詞':
            result.append(sentence[i - 1]['表層形'] + 'の' + sentence[i + 1]['表層形'])
    return result

morpheme_data = parse.get_morpheme_from_neko()
print(parse.flatten(list(map(lambda sentence: get_noun_phrase_from_sentence(sentence), morpheme_data))))
