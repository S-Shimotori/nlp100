import chunks
from functools import reduce


def flatten(items):
    return sum(items, [])


sentences = chunks.get_sentences_as_chunks()


def get_chunk_and_dst(chunk, chunks_for_sentence):
    return chunk, list(map(lambda src: chunks_for_sentence[src], chunk.srcs))


sentences_with_sources = list(map(lambda chunks_for_sentence: list(map(lambda chunk: get_chunk_and_dst(chunk, chunks_for_sentence), chunks_for_sentence)), sentences))
filtered = list(map(
    lambda sentence: list(filter(
        lambda relate: relate[0].has_pos('動詞') and reduce(lambda result, chunk: result or chunk.has_pos('助詞'), relate[1], False),
        sentence[1:])),
    sentences_with_sources
))

relatives = flatten(filtered)


def get_pos(chunk, pos):
    for morph in chunk.morphs:
        if morph.pos == pos:
            return morph

output = open('45/output.txt', 'w')
output.writelines("\n".join(
        list(map(
                lambda relative: "%s\t%s" % (
                    get_pos(relative[0], '動詞').base,
                    ' '.join(list(filter(lambda result: len(result) != 0, list(map(lambda chunk: get_pos(chunk, '助詞').base if chunk.has_pos('助詞') else '', relative[1])))))),
                relatives
        ))))
output.close()
