import queue
import re
from time import sleep
from urllib.parse import urlparse
from urllib.parse import urljoin
#import urllib.robotparser 
from reppy.robots import Robots
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os


def is_absolute(url):
    """Determine whether URL is absolute."""
    return bool(urlparse(url).netloc)

def is_inner_link(url):
    return bool(urlparse(url).path == '' or urlparse(url).path == '/')


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options)
email_addresses = []
seed_page = "https://www.stevens.edu"
q = queue.Queue()
q.put(seed_page)
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.stevens.edu/robots.txt")
robots = Robots.fetch("http://www.stevens.edu/robots.txt")
tagged_urls = [seed_page]


for i in range(50):
    url = q.get()
    print("url: {}".format(url))

    # r = requests.get(url)
    sleep(2) # delay 2 seconds before reading contents
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Get contents
    contents = soup.get_text()

    #save page contents
    dir_path = "./root/"+url[23:]
    os.makedirs(dir_path)
    f = open(dir_path+"/page.html","w+")
    f.write(contents)
    f.close()

    # Extract all email addresses.
    email_addresses += re.findall("\S+@stevens.edu", contents)
    email_addresses = list(set(email_addresses))

    links = soup.find_all('a')
    for link in links:
        u = link.get('href')
        if not is_absolute(u) and not is_inner_link(u):
            u = urljoin(url, u)
        if "stevens.edu" in u:
            #print("URL {0} Can Fetch: {1}".format(u, rp.can_fetch("*", u)))
            allowed = robots.allowed(u,"*")
            #print("URL {0} Can Fetch: {1}".format(u, allowed))
            if allowed:
                if u not in tagged_urls:
                    tagged_urls.append(u)
                    q.put(u)
            # test code
            # u = urljoin(url, "/admin/zzz.html")
            # print("URL {0} Can Fetch: {1}".format(u, robots.allowed(u,"*")))


    print("Queue size: {}".format(q.qsize()))
    print("# email addresses: {}".format(len(email_addresses)))

#save email addresses
with open("email.txt", "w+") as f:
    for e in email_addresses:
        f.write(e + "\n")
