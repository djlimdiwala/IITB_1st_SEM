import string, math
f1 = open("wordcounts.txt","r+");
f3 = open("isyms.txt","w+");
f4 = open("osyms.txt","w+");

sym_i = 1
f3.write("-	0" + "\n")
f4.write("-	0" + "\n")
total = 29757
count = 0
for i in range(total):
	buffer1 = f1.readline()
	buffer2 = buffer1.split(" ")
	count = count + int(buffer2[1])

f1.close()
f1 = open("wordcounts.txt","r+");
f2 = open("Gg.fst","w+");

for i in range(total):
	buffer1 = f1.readline()
	buffer2 = buffer1.split(" ")
	prob = float(buffer2[1]) / count
	prob = - math.log(prob)
	f2.write("0	" + "0 " + "	" + str(buffer2[0]) + "	" + str(buffer2[0]) + "	" + str(prob))
	f2.write("\n")
	f3.write(str(buffer2[0]) + "	" + str(sym_i))
	f3.write("\n")
	f4.write(str(buffer2[0]) + "	" + str(sym_i))
	f4.write("\n")
	sym_i = sym_i + 1
f2.write("0")
f2.write("\n")
f1.close()
f2.close()
f3.close()
f4.close()
