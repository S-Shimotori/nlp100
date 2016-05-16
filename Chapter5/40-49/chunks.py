import morpheme


def get_sentences_as_chunks():
    cabocha = open('../neko.txt.cabocha')
    cabocha_data = cabocha.readlines()
    cabocha.close()
    chunk_strings_list = list(map(lambda sentence: split_sentence_into_chunks(sentence), split_cabocha_into_sentences(cabocha_data)))
    return list(map(lambda sentence: morpheme.set_srcs(list(map(lambda strings: morpheme.create_chunk(strings), sentence))), chunk_strings_list))


def split_cabocha_into_sentences(lines):
    result = []
    sentence = []
    for line in lines:
        if line == "EOS\n":
            if len(sentence) != 0:
                result.append(sentence)
            sentence = []
        elif line != "\n":
            sentence.append(line)
    return result


def split_sentence_into_chunks(lines):
    result = []
    chunk = []
    for line in lines:
        if line.startswith('* '):
            if len(chunk) != 0:
                result.append(chunk)
            chunk = [line]
        else:
            chunk.append(line)
    if len(chunk) != 0:
        result.append(chunk)
    return result
