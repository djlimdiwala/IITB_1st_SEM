import re
f1 = open("input.txt","rw+");
f2 = open("output.txt","rw+");
f3 = open("input.txt","rw+");
f4 = open("input.txt","rw+");



#####   matching valid moblile numbers  #####

for line in f3:
	obj = re.search(r'(\+(91|\(91\))|0)(\d{4}[\s-]?\d{6}|\d{3}[\s-]?\d{7}|\d{2}[\s-]?\d{8})(\s|\$)',line)
	if obj:
		print obj.group()





#####   matching valid Email ID  #####

for line in f4:
	obj = re.search(r'[0-9a-zA-Z]+[.[0-9a-zA-Z]+]?@[a-zA-Z]+(\.[a-zA-Z]+){1,3}(\s|\z)',line)
	if obj:
		print obj.group()






##### substituting valid phone numbers and EMAAIL IDs  ####

#num = re.sub(r'(\+(91|\(91\))|0)(\d{4}[\s-]?\d{6}|\d{3}[\s-]?\d{7}|\d{2}[\s-]?\d{8})\s',r'(\+(91|\(91\))|0)(\d{4}[\s-]?\*\*\*\*\*\*|\d{3}[\s-]?\*\*\*\*\*\*\*|\d{2}[\s-]?\*\*\*\*\*\*\*\*)\s',f1.read())
num = re.sub(r'(\+(91|\(91\))|0)(\d{4}[\s-]?\d{6}|\d{3}[\s-]?\d{7}|\d{2}[\s-]?\d{8})\s{1}',"###valid### ",f1.read())
num1 = re.sub(r'(\+(91|\(91\))|0)(\d{4}[\s-]?\d{6}|\d{3}[\s-]?\d{7}|\d{2}[\s-]?\d{8})\${1}',"###valid###\n",num)
num1 = re.sub(r'[0-9a-zA-Z]+[.[0-9a-zA-Z]+]?@gmail(\.[a-zA-Z]+){1,3}(\s|\z)',"THIS IS GMAIL ID \n",num1)
num1 = re.sub(r'[0-9a-zA-Z]+[.[0-9a-zA-Z]+]?@YAHOO(\.[a-zA-Z]+){1,3}(\s|\z)',"THIS IS YAHOO ID \n",num1)
num1 = re.sub(r'[0-9a-zA-Z]+[.[0-9a-zA-Z]+]?@[a-zA-Z]+(\.[a-zA-Z]+){1,3}(\s|\z)',"tHIS IS PIRVATE MAIL ID \n",num1)
print num1

f2.write(num1)