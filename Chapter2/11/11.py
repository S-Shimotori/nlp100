hightemp = open('../hightemp.txt')
hightemp_data = hightemp.read()
hightemp.close()

output_python = open('output_python.txt', 'w')
output_python.write(hightemp_data.replace("\t", ' '))
output_python.close()

