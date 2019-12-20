import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv 


mails=[]


def findMails(soup):
    for name in soup.find_all('a'):
        if(name is not None):
            emailText=name.text
            match=bool(re.match('\w+@\w+\.{1}\w+',emailText))
            if match==True:
                emailText=emailText.replace(" ",'').replace('\r','')
                emailText=emailText.replace('\n','').replace('\t','')
                if(len(mails)==0)or(emailText not in mails):
                    print(emailText)
                mails.append(emailText)


df = pd.read_csv("entertainment2.csv", usecols = ['HTTP'])

n = 1

while n < 20:
	url = df.loc[n,'HTTP']
#url='https://aohack.com'
	allLinks = []
	response = requests.get(url)
	soup=BeautifulSoup(response.text,'html.parser')
	links = [a.attrs.get('href') for a in soup.select('a[href]') ]
	for i in links:
		if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
			allLinks.append(i)
	allLinks=set(allLinks)
	for link in allLinks:

	    if link.startswith(url): # or link.startswith("www"))
	        if link.endswith('javascript:void(0)'):
	        	continue
	        else:
		        r=requests.get(link)
		        data=r.text
		        soup=BeautifulSoup(data,'html.parser')
		        findMails(soup)


	mails=set(mails)
	if(len(mails)==0):
	    print("NO MAILS FOUND")
		
		


	# Populate CSV with links
	with open('results.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Number", "Website"])
	    for x in range(len(mails)):
	    	writer.writerow([url, pure_links[x]])

	n+=1