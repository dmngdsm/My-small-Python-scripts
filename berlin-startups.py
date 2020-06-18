import requests    # Include HTTP Requests module
import csv 
from bs4 import BeautifulSoup  # Include BS web scraping module
base_url = "https://berlin.startups-list.com/" # Website / URL we will contact
links = []
names = []
about = []
pure_links = []
pure_name = []
pure_about = []
pure_website =[]
pure_facebook = []
pure_twitter = []


current_url = base_url
print(current_url)
#Parse Current URL
r = requests.get(current_url)           # Sends HTTP GET Request
soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response

#Find divs 
headers = soup.find_all('div', attrs={'class':'card'})

#Get names
for div in headers:
	names.append(div.find('h1', attrs={'property':'name'}))
	links.append(div.find('a').get('href'))
	about.append(div.find('p').get_text())
#Get links


	
# for a in names:
# 	pure_name.append(a.text.strip())
	
# print(pure_name)
print(len(links))
print(len(about))
