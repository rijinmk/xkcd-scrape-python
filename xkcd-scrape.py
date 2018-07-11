import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import os
import json
base_url = "http://xkcd.com/"
for i in range(1,1746,1):
    print "opening ", base_url+str(i)
    url = base_url+str(i)
    print "\033[1;31;5mreading data\033[0m"
    try:
        web_data = urllib.urlopen(url).read()
        print "\033[1;36mdata read\033[0m"
        web_soup = BeautifulSoup(web_data)
        web_images = web_soup.findAll("img")
        image_url = "http://"+web_images[1]["src"][2:]
        name = image_url.split("/")[-1]
        print "image url \033[1;97m"+image_url+"\033[0m"
        image_data = urllib.urlopen(image_url).read()
        print "image data aquired"
        print "Creating file: ","xkcd"+str(i+1)+".png"
        f = open("xkcd_names/"+name,"w")
        f.write(image_data)
        f.close()
        print name+" \033[1;36;5mCREATED!\033[0m"
    except:
        print
        print "***************************"
        print "\033[1;91;5mERROR\033[0m"
        print "***************************"
        print
        pass
