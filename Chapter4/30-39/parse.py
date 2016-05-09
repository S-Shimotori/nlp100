from collections import Counter

def flatten(list):
    return sum(list, [])

def parse_mecab(line):
    data = line.rstrip().split("\t")
    morpheme = data[1].split(',')
    return {
            '表層形': data[0],
            '品詞': morpheme[0],
            '品詞細分類1': morpheme[1],
            '品詞細分類2': morpheme[2],
            '品詞細分類3': morpheme[3],
            '活用形': morpheme[4],
            '活用型': morpheme[5],
            '原形': morpheme[6],
            '読み': morpheme[7] if len(morpheme) > 7 else '*',
            '発音': morpheme[8] if len(morpheme) > 8 else '*'
        }

def get_morpheme(mecab_data):
    return list(map(parse_mecab, mecab_data[:-1]))

def split_sentence(morpheme_data):
    result = []
    sentence = []
    for word in morpheme_data:
        sentence.append(word)
        if word['品詞'] == '記号' and (word['品詞細分類1'] == '空白' or word['品詞細分類1'] == '句点'):
            result.append(sentence)
            sentence = []
    if len(sentence) != 0:
        result.append(sentence)
    return result

def get_morpheme_from_neko():
    neko_mecab = open('../neko.txt.mecab')
    neko_mecab_data = neko_mecab.readlines()
    neko_mecab.close()
    return split_sentence(get_morpheme(neko_mecab_data))

def get_word_with_parameter(morpheme_data, condition):
    return flatten(list(map(lambda sentence: list(filter(lambda word: condition(word), sentence)),  morpheme_data)))

def create_tuple_from_word(word):
    return (word["表層形"], word["品詞"], word["品詞細分類1"], word["品詞細分類2"], word["品詞細分類3"], word["活用形"], word["活用型"], word["原形"], word["読み"], word["発音"])

def get_counter_from_words(words):
    return Counter(map(lambda word: create_tuple_from_word(word), words))
