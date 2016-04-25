from functools import reduce

hightemp = open("../hightemp.txt")
hightemp_data = hightemp.readlines()
hightemp.close()

print(list(set(map(lambda line: line.split("\t")[0],hightemp_data))))
