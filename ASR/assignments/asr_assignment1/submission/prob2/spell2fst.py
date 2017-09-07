import string
import os,sys


temp = sys.argv[1].split('=')
odir = temp[1]

temp = sys.argv[2].split('=')
vocab = temp[1]

temp = sys.argv[3].split('=')
dev = temp[0]


f1 = open(dev,"r+")

total = 100
for i in range(total):
	buffer1 = f1.readline()
	buffer2 = buffer1.split('\t')
	id = buffer2[0]
	# print buffer2
	buffer2 = buffer2[2].split('\n')
	# print len(buffer2[0])

	file_name = odir + "/{" + id + "}.fsa.txt"
	f2 = open(file_name, "w+")
	seq = 0
	for j in range(len(buffer2[0])):
			f2.write(str(seq) + "	" + str(seq+1) + "	" + str(buffer2[0][j]))
			f2.write("\n")
			seq =seq + 1
	f2.write(str(seq))
	f2.write("\n")
	f2.close()
	cmd = "fstcompile --acceptor -isymbols=osyms.txt --keep_isymbols " + file_name + " " + file_name
	os.system(cmd)


