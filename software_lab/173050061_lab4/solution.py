import requests , getpass , sys ,bs4 , re



def create_session ():
	
	print '\nWel come to moodle@IITB'
	print '\nLoggong in...'
	while 1:

		# u_name = raw_input("Username :- ")
		# password = getpass.getpass("Password :- ")
		u_name = sys.argv[2]
		password = sys.argv[3]

		payload = {
	    	'action'   : 'login',
	    	'username' : u_name,
	    	'password' : password
		}
		login_url = 'https://moodle.iitb.ac.in/login/index.php'
		session=requests.session()
		result=session.post(login_url, data = payload)
		if result.status_code == 203:
			print 'Error logging in'
			print 'try again.....'

		if result.status_code == 200:
			print 'Successfully logged in.......'
			return session


def open_discussion_page (session):

	result = session.get("http://moodle.iitb.ac.in/my")
	count = 0
	if result.status_code != 200:
		print "Error status"

	html_form = bs4.BeautifulSoup(result.text,'html.parser')
	tag = html_form.find("a", text=re.compile(sys.argv[1]))
	# print tag.text
	course_url = tag['href']
	# print course_url
	result1 = session.get(course_url)
	html_form1 = bs4.BeautifulSoup(result1.text,'html.parser')
	# print html_form1


	tag = html_form1.find("a", href=re.compile('forum'))
	# print (tag.text)
	discuss_url = tag['href']
	# print (discuss_url)

	result1 = session.get(discuss_url)
	html_form1 = bs4.BeautifulSoup(result1.text,'html.parser')
	gg = html_form1.findAll("tr", { "class" : "discussion r0" })
	for tr in gg:
		# print tr
		author1 = re.findall(r'(<td\sclass="author"><a\shref="http://moodle\.iitb\.ac\.in/user/view.php\?id=)(.*?)(">)([A-Za-z\s\.]+)(</a></td>){1}',str(tr))
		if author1:
			# print author1[0][3]
			author = author1[0][3]
			

		gg1 = re.findall(r'(<td\sclass="topic\sstarter"><a\shref=")(http://moodle\.iitb\.ac\.in/mod/forum/discuss\.php\?d=[0-9]+)(">)(.*?)(</a>)',str(tr))
		url = gg1[0][1]
		# print url

		gg1
		result1 = session.get(url)
		html_form1 = bs4.BeautifulSoup(result1.text,'html.parser')
		content = html_form1.findAll("div", { "class" : "posting fullpost" })
		# print content
		gg11 = re.sub(r'<.*?>', "", str(content))
		# print gg11

		result1 = re.findall(r'(https://\.www\.|http://\.www\.|https://|http://|www\.)?(.*?)(\.com|\.in|\.org|\.ac\.in|\.edu)(/[a-zA-Z0-9-&\.#\?])*',gg11)
		# result1 = re.findall(r'\+1',(gg11))

		if result1:
			print "\nFound in this discussion\n" 
			print "Started By :- " + author
			print "Link to the discussion :- " + url
			print "-------------------------------------------------------"
			count = count + 1

	gg = html_form1.findAll("tr", { "class" : "discussion r1" })
	for tr in gg:
		# print tr
		author1 = re.findall(r'(<td\sclass="author"><a\shref="http://moodle\.iitb\.ac\.in/user/view.php\?id=)(.*?)(">)([A-Za-z\s\.]+)(</a></td>){1}',str(tr))
		if author1:
			# print author1[0][3]
			author = author1[0][3]
			

		gg1 = re.findall(r'(<td\sclass="topic\sstarter"><a\shref=")(http://moodle\.iitb\.ac\.in/mod/forum/discuss\.php\?d=[0-9]+)(">)(.*?)(</a>)',str(tr))
		if gg1:
			url = gg1[0][1]
		result1 = session.get(url)
		html_form1 = bs4.BeautifulSoup(result1.text,'html.parser')
		content = html_form1.findAll("div", { "class" : "posting fullpost" })
		gg11 = re.sub(r'<.*?>', "", str(content))


		result1 = re.findall(r'(https://\.www\.|http://\.www\.|https://|http://|www\.)?(.*?)(\.com|\.in|\.org|\.ac\.in|\.edu)(/[a-zA-Z0-9-\+\.#\?=&_])*',gg11)


		if result1:
			print "\nFound in this discussion\n" 
			print "Started By :- " + author
			print "Link to the discussion :- " + url
			print "-------------------------------------------------------"
			count = count + 1

	if count == 1:
		print '\nValid URLs are shared in only one discussion thread in this course discussion'
		print "\n-------------------------------------------------------"

	if count > 1:
		print '\nValid URLs are shared in ' + str(count) + ' discussion threads by different users in this course discussion'
		print "\n-------------------------------------------------------"

	if count == 0:
		print ' \nNo valid URLs are shared in any discussion thread in this course discussion'
		print "\n-------------------------------------------------------"

	return


session = create_session()
open_discussion_page (session)



