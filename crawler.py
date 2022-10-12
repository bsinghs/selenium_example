import queue
import re
from urllib.parse import urlparse
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def is_absolute(url):
    """Determine whether URL is absolute."""
    return bool(urlparse(url).netloc)


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options)


email_addresses = []

q = queue.Queue()

q.put("https://www.stevens.edu/school-business/faculty")

for i in range(600):
    url = q.get()

    # r = requests.get(url)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract all email addresses.
    # print(soup.get_text())
    email_addresses += re.findall("\S+@stevens.edu", soup.get_text())
    email_addresses = list(set(email_addresses))

    links = soup.find_all('a')
    for link in links:
        u = link.get('href')
        if not is_absolute(u):
            u = urljoin(url, u)
        if "stevens.edu" in u:
            q.put(u)

    print("Queue size: {}".format(q.qsize()))
    print("# email addresses: {}".format(len(email_addresses)))

with open("email.txt", "w+") as f:
    for e in email_addresses:
        f.write(e + "\n")
