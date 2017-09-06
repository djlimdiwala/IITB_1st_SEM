Landline phone numbers in india are of ten digits in which first 2-4 digits are STD codes and after that 6-8 digits are actual numbers. So if STD code is 2 digits then phone number is 8 digits. if STD code is 3 digits then phone number is 7 digits. if STD code is 4 digits then phone number is 6 digits. +91 or +(91) or 0 are placed before these numbers for country code.
So, some accepting phone numbers are :-
+912611420500
+91261 1420500
+91261-1420500
+(91)261 1420500
+(91)261-1420500
0261 1420500
026 11420500
etc


Non accepting :- 
+91261142050014
+91261 41420500
+926114205004
026  11420500
etc


While masking, STD codes are masked with **** from valid phone numbers. For example,

+91****1420500
 +91****1420500
+91****1420500
+(91)****1420500
+(91)****1420500








-----------------------------------------------------------------------

MAILIDs are accepted in the following form:-

(somwe text)(.some text{zero or more times})@(some text)(.some text{1 to 3 times})

Example accepting emailIDs :-
dhaval.limdiwala@gmail.com
dhaval@gmail.com
dhaval.limdiwala@gmail.com
djlimdiwala@avanti.co.in
173050061@iitb.ac.in


Non accepting :- 
dhaval.limdiwala@gmail.
dhaval.limdiwala@gmaildhaval.limdiwala@g.com
@gmail.com
@dhaval.limdiwala@gmail.com




MASKING is done in the way that from every valid mail ID, part after @ and before first . after @ is masked with #####. For example, 

dhaval.limdiwala@#####.com
dhaval@#####.com
dhaval.limdiwala@#####.com djlimdiwala@#####.in
djlimdiwala@#####.in
173050061@#####.in



--------------------------------------------------------------------------------

This code contains four regular expressions out of which three are similiar and used for different digit combinations for landline number . For example,
2 digit STD code and 8 digit phone number
3 digit STD code and 7 digit phone number
4 digit STD code and 6 digit phone number


fourth reg. expression is used to find valid E-mails addresses.

---------------------------------------------------------------------------------

Here text to be searched is in input.txt file. Masked output is stored in output.txt file.

Run $ python solution.py


