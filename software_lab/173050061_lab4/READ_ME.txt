In this code, valid URLs which are shared by users in any discussion are found and author  and link of that discussion thread are displayed . At the end total number of threads are displayed.

URLs are found in this way :- 

first there will be https://.www. OR http://.www. OR https:// OR http:// OR www.
second part will be namr of the website i.e flipkart or iitb etc
third part will be .com OR .in OR .org OR .edu OR .ac.in OR .in (for now)
fourth part will be optional. It will be for subpages in website for example = /index/login.php , /mod/forum/discuss.php etc..


Some valid URLs can be --

http://moodle.iitb.ac.in/mod/forum/discuss.php?d=62797
https://www.tutorialspoint.com/python/python_reg_expressions.htm
iitb.ac.in
www.flipkart.com


Some Invalid URLs can be --
htt.www.com
https://flipkart
www.flipkart.fgb


==================================================================


Here are URLs that are being accessed --

User's home page :-  http://moodle.iitb.ac.in/my/
Subject's home page :- http://moodle.iitb.ac.in/course/view.php?id=5597  (this one is of software lab)
News Forum page :- http://moodle.iitb.ac.in/mod/forum/view.php?id=41349 (where all discussions are displayed)


==================================================================


This code will take three command line arguments --
1. course number. for example for software lab it would be 699
2. Username of moodle
3. password for moodle

In terminal, write the following command - 

$ python solution.py <course number> <Username> <password>

It will show output in which It will show name who started that discussion and link of that discussion in which valid URLs is found. 
At the end It will show total occurences of valid URLs In all threads.



The output would look like this --

Wel come to moodle@IITB

Loggong in...
Successfully logged in.......






Found in this discussion

Started By :- RANGARI AKASH ANAND
Link to the discussion :- http://moodle.iitb.ac.in/mod/forum/discuss.php?d=63084
-------------------------------------------------------


Found in this discussion

Started By :- Om P. Damani  
Link to the discussion :- http://moodle.iitb.ac.in/mod/forum/discuss.php?d=61140
-------------------------------------------------------

.
.
.
.
.
.
.



Valid URLs are shared in 5 discussion threads by different users in this course discussion

-------------------------------------------------------






