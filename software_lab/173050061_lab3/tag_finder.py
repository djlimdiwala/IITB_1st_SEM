import re
f1 = open("index.html","r+");
f2 = open("tag.txt","a+");
f2.truncate()



for line in f1:
	obj = re.findall(r'(<)([a-zA-Z]+)(>)',line)
	if obj:
		print obj
		for i in range(len(obj)):
			f2.write(obj[i][1])
			f2.write("\n")
f1.close()
f2.close()

f3 = open("tag.txt","r").readlines()
lines_set = set(f3)
f3 = open("tag.txt","w")
for line in lines_set:
    f3.write(line)
f3.close()