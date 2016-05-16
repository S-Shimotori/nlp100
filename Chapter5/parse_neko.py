import CaboCha

neko = open('neko.txt')
neko_data = neko.readlines()
neko.close()

parser = CaboCha.Parser()

output = open('neko.txt.cabocha', 'w')
output.write("\n".join(list(map(lambda sentence: parser.parse(sentence).toString(CaboCha.FORMAT_LATTICE), neko_data))))
output.close()
