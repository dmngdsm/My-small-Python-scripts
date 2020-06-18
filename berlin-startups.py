import requests    # Include HTTP Requests module
import csv 
from bs4 import BeautifulSoup  # Include BS web scraping module
base_url = "https://berlin.startups-list.com/" # Website / URL we will contact
links = []
names = []
about = []


current_url = base_url
print(current_url)

#Parse Current URL
r = requests.get(current_url)           # Sends HTTP GET Request
soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response

#Find divs 
headers = soup.find_all('div', attrs={'class':'card'})

#Get names, websites and about
for div in headers:
	names.append(div.find('h1', attrs={'property':'name'}).get_text())
	links.append(div.find('a').get('href'))
	about.append(div.find('p').get_text())


# Populate CSV with info
	with open('berlin-startups-list.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Name", "About", "Website"])
	    for i in range(len(names)):
	    	writer.writerow([names[i], about[i],links[i]])


	
print('scrapie readie')


