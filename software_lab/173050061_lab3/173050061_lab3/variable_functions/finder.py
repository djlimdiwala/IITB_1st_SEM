import re
f1 = open("reverse.c","r+");
f2 = open("variable.txt","a+");
f3 = open("function.txt","a+");
f2.truncate()
f3.truncate()


#  This finds variables from the C file and copies them in variable.txt file#
for line in f1:
	obj = re.findall(r'(int|float|double){1}(\s)?([a-zA-Z0-9\,=\s]+)([\s]*;)',line) #regular expression to find variables
	if obj:
		
		for i in range(len(obj)):
			p = obj[i][2].split(",")
			for i in range(0,len(p)):
	 			f2.write(p[i])
	 			f2.write("\n")
f1.close()



f1 = open("reverse.c","r+");

#  This finds functions from the C file and copies them in function.txt file#
for line in f1:
	obj = re.findall(r'(=\s|=)?([a-zA-Z0-9_]+)(\([a-zA-Z0-9\,=\s_%"&]*\)|\(\))([\s]*;)?',line) #regular expression to find functions
	if obj:
		for i in range(len(obj)):
			f3.write(obj[i][1])
			f3.write("\n")
	

f2.close()
f3.close()
f1.close()




#removes duplicates from function.txt
f3 = open("function.txt","r").readlines()
lines_set = set(f3)
f3 = open("function.txt","w")
for line in lines_set:
    f3.write(line)
f3.close()


#removes duplicates from variable.txt
f3 = open("variable.txt","r").readlines()
lines_set = set(f3)
f3 = open("variable.txt","w")
for line in lines_set:
    f3.write(line)
f3.close()



#regular expression to remove some exeptions 
f2 = open("variable.txt","r+")
f3 = open("function.txt","r")

num = re.sub(r'(if|while|for|else)(\n)',"",f3.read())
f3.close()
f3 = open("function.txt","w+")
f3.write(num)
f3.close()


#regular expression to remove variable values
num = re.sub(r'([a-zA-Z0-9]+)(\s=\s[a-zA-Z0-9"]+|=[a-zA-Z0-9"]+)',r'\1',f2.read())
f3 = open("variable.txt","w+")
f3.write(num)
f3.close()




