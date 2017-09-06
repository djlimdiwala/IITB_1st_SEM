import re
f1 = open("input.txt","r+");
f2 = open("output.txt","w+");




p = f1.read()

#regular expression to find landline number with 3 digit STD code and 7 digit phone number
num = re.sub(r'(\+91|\+\(91\)|0)(\d{3})([\s-]?)(\d{7})(\s|\$)',r'\1****\4\5',p)

#regular expression to find landline number with 2 digit STD code and 8 digit phone number
num = re.sub(r'(\+91|\+\(91\)|0)(\d{2})([\s-]?)(\d{8})(\s|\$)',r'\1****\4\5',num)

#regular expression to find landline number with 4 digit STD code and 6 digit phone number
num = re.sub(r'(\+91|\+\(91\)|0)(\d{4})([\s-]?)(\d{6})(\s|\$)',r'\1****\4\5',num)


#regular expression to find valid EMail address
num = re.sub(r'([0-9a-zA-Z]+[.[0-9a-zA-Z]+]?@)([a-zA-Z]+)(\.[a-zA-Z]+){1,3}(\s|\$)',r'\1#####\3\4',num)

f2.write(num)
f1.close()
f2.close()



