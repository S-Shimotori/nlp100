from functools import reduce


class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def create_morph(line):
    splitted = line.split("\t")
    data = splitted[1].split(',')
    return Morph(splitted[0], data[6], data[0], data[1])


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def get_surfaces(self):
        return reduce(lambda result, morph: result + morph.surface, self.morphs, '')

    def get_surfaces_without_symbol(self):
        return reduce(lambda result, morph: result + morph.surface, filter(lambda morph: morph.pos != '記号', self.morphs), '')

    def has_pos(self, pos):
        return reduce(lambda result, morph: result or morph.pos == pos, self.morphs, False)


def create_chunk(lines):
    splitted = lines[0].split(' ')
    return Chunk(list(map(lambda line: create_morph(line), lines[1:])), int(splitted[2][:-1]), [])


def set_srcs(chunks):
    for i, chunk in enumerate(chunks):
        dst = int(chunk.dst)
        if dst > 0:
            chunks[dst].srcs.append(i)
    return chunks
