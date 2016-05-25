import chunks


sentences = chunks.get_sentences_as_chunks()

def get_chunk_and_dst(chunk, chunks_for_sentence):
    return (chunk, chunks_for_sentence[chunk.dst] if chunk.dst > 0 else None)


relates = list(map(lambda chunks_for_sentence: list(map(lambda chunk: get_chunk_and_dst(chunk, chunks_for_sentence), chunks_for_sentence)), sentences))


filtered = list(map(lambda sentence: list(filter(lambda relate: relate[0].has_pos('名詞') and relate[1].has_pos('動詞'), sentence[:-1])), relates))

remove_empty = list(filter(lambda noun_and_verb: len(noun_and_verb) != 0, filtered))

print("\n".join(list(map(lambda sentence: "\n".join(list(map(lambda relate: "%s\t%s" % (relate[0].get_surfaces_without_symbol(), relate[1].get_surfaces_without_symbol()), sentence))), remove_empty))))
