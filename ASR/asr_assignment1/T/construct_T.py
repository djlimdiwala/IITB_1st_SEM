import string
f1 = open("words.txt","r+");
f2 = open("Tt.fst","w+");
f3 = open("isyms.txt","w+");
f4 = open("osyms.txt","w+");
flag = 0
global_counter = 2

# 29758
f3.write("-	0")
f3.write("\n")
f4.write("-	0")
f4.write("\n")
alphabet= string.ascii_lowercase
count = 1
for letter in alphabet:
	f4.write(letter + "	" + str(count))
	f4.write("\n")
	count = count + 1

for i in range(29758):
	buffer1 = f1.readline()
	buffer2 = buffer1[0:len(buffer1)-1]
	f3.write(buffer2 + "	" + str(i+1))
	f3.write("\n")
	f4.write(buffer2 + "	" + str(count))
	count = count + 1
	f4.write("\n")
	k = 0
	if len(buffer2) == 1:
		f2.write("0	" + "1" + "	" + buffer2 + "	" + buffer2)
		f2.write("\n")
		continue


	for letter in buffer2:
		if k == 0:
			f2.write("0	" + str(global_counter) + "	" + buffer2 + "	" + letter)
			f2.write("\n")
			k =k + 1
		elif k == len(buffer2)-1:
			f2.write(str(global_counter) + "	" + "1" + "	" + "-" + "	" + letter)
			f2.write("\n")
			global_counter = global_counter + 1
			k =k + 1
		else:
			t = global_counter + 1
			f2.write(str(global_counter) + "	" + str(t) + "	" + "-" + "	" + letter)
			f2.write("\n")
			global_counter = global_counter + 1
			k =k + 1

f2.write("1")
f2.write("\n")



f1.close()
f2.close()
f3.close()
f4.close()