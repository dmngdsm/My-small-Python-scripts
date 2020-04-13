import requests    # Include HTTP Requests module
import csv 
from bs4 import BeautifulSoup  # Include BS web scraping module
base_url = "https://www.viamichelin.com/web/Restaurants/Restaurants-Germany" # Website / URL we will contact
links = []
pure_address =[]
pure_names = []
pure_stars = []
pure_city = []



for stars in range(1,2):
	current_url = base_url+"?stars="+str(stars)
	# +"&page=6"
	print(current_url)
	#Parse Current URL
	r = requests.get(current_url)           # Sends HTTP GET Request
	soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
		
	#Find divs 
	headers = soup.find_all('div', attrs={'class':'poi-item-details truncate'})

	#Get addresses
	for div in headers:
		x= div.get_text()
		# pure_address.append(x.split("-", 1).pop(1))
		pure_address.append(x)
		y = x.split()
		city = y[-1]
		pure_city.append(city)


	
	#Get names
	names = soup.find_all('a', attrs={'class':'truncate'})
	for name in names:
		pure_names.append(name.get_text()) 
		pure_stars.append(stars)
			  
	# Populate CSV with info
	with open('restaurants-germany' + str(stars) +'.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Name", "Address", "Stars", "City"])
	    for i in range(len(pure_address)):
	    	writer.writerow([pure_names[i], pure_address[i],pure_stars[i], pure_city[i]])

	pure_address =[]
	pure_names = []
	pure_stars = []
	pure_city = []

