hightemp = open('../hightemp.txt')
hightemp_data = hightemp.readlines()
hightemp.close()

def get_column(index, data):
    return "\n".join(list(map(lambda line: line.split("\t")[index], data)))

col1_python = open('col1_python.txt', 'w')
col1_python.write(get_column(0, hightemp_data))
col1_python.close()

col2_python = open('col2_python.txt', 'w')
col2_python.write(get_column(1, hightemp_data))
col2_python.close()
