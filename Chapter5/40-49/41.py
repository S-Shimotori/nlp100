import chunks


chunks_8 = chunks.get_sentences_as_chunks()[7]
keys = range(0, len(chunks_8) - 1)

print("\n".join(list(map(lambda chunk: "[%d]%s → %d(%s)" % (chunk[0], chunk[1].get_surfaces(), chunk[1].dst, chunks_8[chunk[1].dst].get_surfaces() if chunk[1].dst > 0 else 'null'), zip(keys, chunks_8)))))
