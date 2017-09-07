import string
f1 = open("Ee.fst","w+");

alphabet= string.ascii_lowercase

for letter in alphabet:
	f1.write("0" + "	" + "0" + "	" + str(letter) + "	" + str(letter) + "	" + "0")
	f1.write("\n")

for letter in alphabet:
	f1.write("1" + "	" + "1" + "	" + str(letter) + "	" + str(letter) + "	" + "0")
	f1.write("\n")

for letter in alphabet:
	f1.write("0" + "	" + "1" + "	" + "-" + "	" + str(letter) + "	" + "1")
	f1.write("\n")
	f1.write("0" + "	" + "1" + "	" + str(letter) + "	" + "-" + "	" + "1")
	f1.write("\n")
alphabet1 = alphabet
for letter in alphabet:
	p = letter
	# f1.write("0" + "	" + "1" + "	" + str(p) + "	" + "-" + "	" + "1")
	# f1.write("\n")
	# f1.write("0" + "	" + "1" + "	" + "-" + "	" + str(p) + "	" + "1")
	# f1.write("\n")
	for letter in alphabet1:
		if p != letter:
			f1.write("0" + "	" + "1" + "	" + str(p) + "	" + str(letter) + "	" + "1")
			f1.write("\n")


# f1.write("0" + "	" + "0" + "	" + "-" + "	" + "-" + "	" + "0")
# f1.write("\n")
# f1.write("1" + "	" + "1" + "	" + "-" + "	" + "-" + "	" + "0")
# f1.write("\n")
# f1.write("0" + "	" + "1" + "	" + "-" + "	" + "<eps>" + "	" + "1")
# f1.write("\n")
# f1.write("0" + "	" + "1" + "	" + "<eps>" + "	" + "-" + "	" + "1")
# f1.write("\n")
f1.write("1")
f1.write("\n")
f1.write("0")
f1.write("\n")
f1.close()
