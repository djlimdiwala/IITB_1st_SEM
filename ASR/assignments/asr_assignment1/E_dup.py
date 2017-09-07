import subprocess
import os

f1 = open("assgmt1/dev.txt",  "r+")
counter = 0
total = 100
for i in range(total):
	buffer1 = f1.readline()
	buffer2 = buffer1.split('\t')
	id = buffer2[0]
	correct = buffer2[1]
	name = "dev_wrd/{" + str(id) + "}.fsa.txt"
	
	cmd = "fstarcsort --sort_type=olabel " + name + " " + name
	os.system(cmd)
	os.system("fstarcsort --sort_type=ilabel E_dup.fst E_dup.fst")
	cmd = "fstcompose " + name + " E_dup1.fst me.fst"
	os.system(cmd)
	os.system("fstarcsort --sort_type=olabel me.fst me.fst")
	os.system("fstarcsort --sort_type=ilabel TI.fst TI.fst")
	os.system("fstcompose me.fst TI.fst met.fst")
	os.system("fstarcsort --sort_type=olabel met.fst met.fst")
	os.system("fstarcsort --sort_type=ilabel G.fst G.fst")
	os.system("fstcompose met.fst G.fst metg.fst")
	os.system("fstprint --isymbols=isyms.txt --osymbols=osyms.txt metg.fst text.fst")
	o = input()
	os.system("fstpush --push_weights --push_labels metg.fst metg.fst")
	os.system("fstprint --isymbols=isyms.txt --osymbols=osyms.txt metg.fst text.fst")
	os.system("fstdraw --isymbols=isyms.txt --osymbols=osyms.txt metg.fst metg.dot")
	os.system("dot -Tps metg.dot >metg.ps")
	os.system("fstprint --isymbols=isyms.txt --osymbols=osyms.txt metg.fst text.fst")

	f2 = open("text.fst",  "r+")
	import os
	prob = 1000
	prob_word = ""
	if os.stat("text.fst").st_size > 0:
		
		i = 0
		while True:
			line = f2.readline()
			if not line:
				break
			# print line
			proc = line.split('\t')
			# print proc
			if len(proc) == 1:
				break
			pr = proc[3].split('\n')
			if pr[0] != '-':
				# print proc[3]
				if proc[4] != '-':

					pr = proc[4].split('\n')
					pr1 = pr[0]
					# print float(pr2)
					if float(pr1) <= prob and proc[2] == "<eps>":
						prob_word = proc[2]
						prob = float(pr1)

		if prob_word == correct:
			counter = counter + 1
	print counter
	print prob
	print prob_word + "\n"

	o = input()
print counter



