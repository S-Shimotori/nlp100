import chunks


def flatten(list):
    return sum(list, [])

morphs = list(map(lambda sentence: flatten(list(map(lambda chunk: chunk.morphs, sentence))), chunks.get_sentences_as_chunks()))
print(list(map(lambda morph: "%s %s %s %s" % (morph.surface, morph.base, morph.pos, morph.pos1), morphs[2])))
