import json, requests, sys , webbrowser , subprocess
import os

def get_data(url, as_bytes=False):
	response = requests.get(url)
	response.raise_for_status()
	if (not as_bytes):
		return response.text
	else:
		return response.content


if len(sys.argv) > 1:
    village = ' '.join(sys.argv[1:])


url = "https://gsda.maharashtra.gov.in/maps/data.js"
response = requests.get(url)
response.raise_for_status()
districts = json.loads(response.text)

region_list = []
district_list = []
taluks_list = []
village_list = []
village_name = []

for i in range(len(districts)):

	url = "https://gsda.maharashtra.gov.in/maps/" + districts[i] + "/data.js"
	region = districts[i]

	response = requests.get(url)
	response.raise_for_status()
	data = json.loads(response.text)
	
	for key in data:
		key1 = key
		d = data[key]
		for key in d:
			key2 = key
			p = data[key1][key2]
			for key in p:
				key3 = key
				if village.lower() == key.lower():
					region_list.append(region)
					district_list.append(key1)
					taluks_list.append(key2)
					village_name.append(key3)
					village_list.append(data[key1][key2][key3])
					break


if len(region_list) == 0 :
	print ("\n" + "No village found named " + village + "\n")
n = 2

if len(region_list) > 1 :
	print ("\n" + "Multiple villages with same name...")
	print ("Enter number to choose particular village ")
	for i in range(len(region_list)):
		print ("\n" + " " + str(i+1) +".  " + str(region_list[i]) + "  " + str(district_list[i]) + "  " + str(taluks_list[i]) + "  " + str(village_name[i]))
	choice = input("\n" + "  Enter your choice :- ")
	url = "https://gsda.maharashtra.gov.in/maps/" + region_list[int(choice)-1] + "/" + district_list[int(choice)-1] +  "/" + taluks_list[int(choice)-1] +  "/" + village_list[int(choice)-1]
	content = get_data(url, True)
	f1 = open("map.pdf","wb+")
	f1.write(content)
	f1.close()
	webbrowser.open("map.pdf", new=n)




if len(region_list) == 1 :
	url = "https://gsda.maharashtra.gov.in/maps/" + region_list[0] + "/" + district_list[0] +  "/" + taluks_list[0] +  "/" + village_list[0]
	content = get_data(url, True)
	f1 = open("map.pdf","wb+")
	f1.write(content)
	f1.close()
	webbrowser.open("map.pdf")