import sys

N = int(sys.argv[1])

hightemp = open('../hightemp.txt')
hightemp_data = hightemp.readlines()
hightemp.close()

output_python = open('output_python.txt', 'w')
index = N if N < len(hightemp_data) else len(hightemp_data)
output_python.write(''.join(hightemp_data[:index]))
output_python.close()
