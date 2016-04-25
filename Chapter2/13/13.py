col1 = open('../12/col1_python.txt')
col2 = open('../12/col2_python.txt')
zipped = zip(col1.readlines(), col2.readlines())
col1.close()
col2.close()

output_python = open('output_python.txt', 'w')
output_python.write("\n".join(list(map(lambda t: t[0].strip() + "\t" + t[1].strip(), zipped))))
output_python.close()
