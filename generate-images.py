import requests
import time
import csv




#1. define function that creates link. If value =="default" it uses a set link, else it appends the word to a url
def setlink(caption, keyword):
	
	global image_url
	default_url = "https://source.unsplash.com/random"
	
	if keyword == "default":
		image_url = "https://placid.app/u/bdn5ebdno?picture-0=" + default_url + "&img=%24DEFAULT%24&quote=" + caption + "&subtitle=%24DEFAULT%24"
	else:
		image_url = "https://placid.app/u/bdn5ebdno?picture-0=https://source.unsplash.com/weekly?" + keyword + "&img=%24DEFAULT%24&quote=" + caption + "&subtitle=%24DEFAULT%24"
	return image_url


#2. define download function

def downloadimg(heading):
	print(requests.get(image_url).text)
	time.sleep(5)  #set freeze time to be able to generate image

	img_data = requests.get(image_url).content

	with open(heading + ".jpg", 'wb') as handler:
	    handler.write(img_data)


#3. iterate through arrays and download images

with open('sheet1.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    
    for i in reader:
    	setlink(i[0],i[1])
    	downloadimg(i[0])
    	time.sleep(2)
    	


