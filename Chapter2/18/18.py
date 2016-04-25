hightemp = open("../hightemp.txt")
hightemp_data = hightemp.readlines()
hightemp.close()

print(sorted(hightemp_data, key=lambda line: float(line.split("\t")[2]), reverse=True))
