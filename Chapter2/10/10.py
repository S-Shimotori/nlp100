hightemp = open('../hightemp.txt')
print(sum(1 for line in hightemp))
hightemp.close()
