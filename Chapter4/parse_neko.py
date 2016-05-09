import MeCab

neko = open('neko.txt')
neko_data = ''.join(neko.readlines())
neko.close()

mt = MeCab.Tagger()

output = open('neko.txt.mecab', 'w')
output.write(mt.parse(neko_data))
output.close()
