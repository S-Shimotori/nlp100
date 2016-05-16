import chunks


sentences = chunks.get_sentences_as_chunks()


def get_relates_string(chunk, chunks_for_sentence):
    return "%s%s" % (chunk.get_surfaces_without_symbol(), "\t" + chunks_for_sentence[chunk.dst].get_surfaces_without_symbol() if chunk.dst > 0 else '')


print("\n".join(list(map(lambda chunks_for_sentence: "\n".join(list(map(lambda chunk: get_relates_string(chunk, chunks_for_sentence), chunks_for_sentence))), sentences))))
