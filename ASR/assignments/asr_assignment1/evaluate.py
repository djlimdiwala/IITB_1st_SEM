import subprocess
import os
import sys

temp = sys.argv[1].split('=')
dev_word = temp[1]

temp = sys.argv[2].split('=')
E_fst = temp[1]

temp = sys.argv[3].split('=')
T_fst = temp[1]

temp = sys.argv[4].split('=')
G_fst = temp[1]

dev_file = sys.argv[5]

f1 = open(dev_file,  "r+")
f2 = open(dev_file,  "r+")
num_lines = sum(1 for line in f2)
f2.close()

counter = 0
total = 100
for i in range(num_lines):
	buffer1 = f1.readline()
	buffer2 = buffer1.split('\t')
	id = buffer2[0]
	correct = buffer2[1]
	name = dev_word + "/{" + str(id) + "}.fsa.txt"
	
	cmd = "fstarcsort --sort_type=olabel " + name + " " + name
	os.system(cmd)
	os.system("fstarcsort --sort_type=ilabel " + E_fst + " " + E_fst)
	os.system("fstcompose " + name + " " + E_fst + " me.fst")
	os.system("fstarcsort --sort_type=olabel me.fst me.fst")
	os.system("fstinvert " + T_fst + " TI.fst" )
	os.system("fstarcsort --sort_type=ilabel TI.fst TI.fst")
	os.system("fstcompose me.fst TI.fst met.fst")
	os.system("fstarcsort --sort_type=olabel met.fst met.fst")
	os.system("fstarcsort --sort_type=ilabel " + G_fst + " " + G_fst)
	os.system("fstcompose met.fst " + G_fst + " " + "metg.fst")
	os.system("fstprint metg.fst text.fst")
	os.system("fstpush --push_weights metg.fst metg1.fst")
	os.system("fstshortestpath metg.fst metg2.fst")
	os.system("fstprint metg1.fst text1.fst")
	os.system("fstprint metg2.fst text.fst")

	f2 = open("text.fst",  "r+")
	import os
	prob = 1000
	prob_word = ""
	if os.stat("text.fst").st_size > 0:
		
		line = f2.readline()
		proc = line.split('\t')

		if proc[3] == correct:
			counter = counter + 1
	# print counter
	# print prob
	# print prob_word + "\n"
	# o = input()

print counter



