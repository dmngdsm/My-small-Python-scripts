import requests    # Include HTTP Requests module
import csv 
import time	#to set sleep function 
from datetime import datetime	    # to see how long it took to execute      
from bs4 import BeautifulSoup  # Include BS web scraping module
startTime = datetime.now()
base_url = "https://a-ads.com/catalog?Category_10_" # Website / URL we will contact
# links = []
pure_links =[]


#Build Current URL
i = 1
while i < 153:	#Pages depend on how much subpages each category has. If you try unexisting page it just loads the first one, so I couldn't use "if r.status_code ...
	if i % 10 == 0:	#Set 10 sec sleep on every 10 requests
		time.sleep(15)
	links = []
	url = base_url + "page=" + str(i) + '&category_id=96&target_type=Category"' #I took categories manually, because it wasn't worth automating
	#Parse Current URL
	r = requests.get(url)           # Sends HTTP GET Request
	soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
	
	#Find divs that contain the <a>
	headers = soup.find_all('div', attrs={'class':'title'})

	#Append websites to a temporary array
	for div in headers:
	    links.append(div.find('a', attrs={'data-remote':'true'}))

	  
	#Populate links array with only the website links
	for a in links[8:-9]: #Results beyond these indexes are not websites
	    pure_links.append(a.text)
	    print(a.text)

	i+=1


# Populate CSV with links
with open('entertainment.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Number", "Website"])
    for i in range(len(pure_links)):
    	writer.writerow([i, pure_links[i]])


print(datetime.now() - startTime) # print how long it took to execute script


