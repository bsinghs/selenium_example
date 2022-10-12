This code crawls the Stevens website looking for Stevens email addresses, creating a text file with one email address per line, while also storing all the pages visited. Uploads the list of email addresses.

Crawler uses followiing:

1. Make use of the Requests module, Selenium, BeautifulSoup, and regular expressions. 

2. Start the search with the seed https://www.stevens.edu/

3. Save all visited pages to disk using a directory structure that reflectes the hierarchy in the URL.

4. Avoid visiting any page more than once. You'll need some way to store the URLs of the pages that have been visited thus far.

5. Obey the robots.txt file, https://docs.python.org/3/library/urllib.robotparser.html,Links to an external site. except that you may set your crawl delay to less than 10 seconds. (However, you should add some crawl delay, however short.)
  
  * Unable to use https://docs.python.org/3/library/urllib.robotparser.html (its not allowing to crawl any page) 
  so using another library called reppy (https://github.com/seomoz/reppy) 
