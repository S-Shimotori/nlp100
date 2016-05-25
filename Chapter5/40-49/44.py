import chunks
from graphviz import Digraph

sentences = chunks.get_sentences_as_chunks()


def get_chunk_and_dst(chunk, chunks_for_sentence):
    return (chunk, chunks_for_sentence[chunk.dst] if chunk.dst > 0 else None)


relates = list(map(lambda chunks_for_sentence: list(map(lambda chunk: get_chunk_and_dst(chunk, chunks_for_sentence), chunks_for_sentence)), sentences))
sentence = relates[7]

graph = Digraph(format='png')
graph.attr('node', shape='circle')

for index, relate in enumerate(sentence):
    graph.node(str(index), relate[0].get_surfaces_without_symbol())

for index, relate in enumerate(sentence):
    if relate[1] != None:
        graph.edge(str(index), str(relate[0].dst))

graph.render('output')
