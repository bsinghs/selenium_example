PS C:\Users\bhaja\dev\selenium_example> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\bhaja\dev\selenium_example>
(venv) PS C:\Users\bhaja\dev\selenium_example>
(venv) PS C:\Users\bhaja\dev\selenium_example>
(venv) PS C:\Users\bhaja\dev\selenium_example>



(venv) PS C:\Users\bhaja\dev\selenium_example> pip install selenium
Collecting selenium
  Downloading selenium-4.5.0-py3-none-any.whl (995 kB)
     |████████████████████████████████| 995 kB 6.4 MB/s
Collecting trio~=0.17
  Downloading trio-0.22.0-py3-none-any.whl (384 kB)
     |████████████████████████████████| 384 kB ...
Collecting trio-websocket~=0.9
  Downloading trio_websocket-0.9.2-py3-none-any.whl (16 kB)
Collecting urllib3[socks]~=1.26
  Using cached urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
Collecting certifi>=2021.10.8
  Using cached certifi-2022.9.24-py3-none-any.whl (161 kB)
Collecting exceptiongroup>=1.0.0rc9
  Downloading exceptiongroup-1.0.0rc9-py3-none-any.whl (12 kB)
Collecting cffi>=1.14
  Downloading cffi-1.15.1-cp310-cp310-win_amd64.whl (179 kB)
     |████████████████████████████████| 179 kB ...
Collecting attrs>=19.2.0
  Downloading attrs-22.1.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB ...
Collecting idna
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting async-generator>=1.9
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting sortedcontainers
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Collecting sniffio
  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)
Collecting outcome
  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     |████████████████████████████████| 118 kB 6.8 MB/s
Collecting wsproto>=0.14
  Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)
Collecting PySocks!=1.5.7,<2.0,>=1.5.6
  Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
Collecting h11<1,>=0.9.0
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB ...
Installing collected packages: pycparser, attrs, sortedcontainers, sniffio, outcome, idna, h11, exceptiongroup, cffi, async-generator, wsproto, urllib3, trio, PySocks, trio-websocket, certifi, selenium
Successfully installed PySocks-1.7.1 async-generator-1.10 attrs-22.1.0 certifi-2022.9.24 cffi-1.15.1 exceptiongroup-1.0.0rc9 h11-0.14.0 idna-3.4 outcome-1.2.0 pycparser-2.21 selenium-4.5.0 sniffio-1.3.0 sortedcontainers-2.4.0 trio-0.22.0 trio-websocket-0.9.2 urllib3-1.26.12 wsproto-1.2.0
WARNING: You are using pip version 21.2.3; however, version 22.2.2 is available.
You should consider upgrading via the 'C:\Users\bhaja\dev\selenium_example\venv\Scripts\python.exe -m pip install --upgrade pip' command.





(venv) PS C:\Users\bhaja\dev\selenium_example> pip install webdriver_manager
Collecting webdriver_manager
  Downloading webdriver_manager-3.8.3-py2.py3-none-any.whl (26 kB)
Collecting requests
  Using cached requests-2.28.1-py3-none-any.whl (62 kB)
Collecting tqdm
  Downloading tqdm-4.64.1-py2.py3-none-any.whl (78 kB)
     |████████████████████████████████| 78 kB 3.4 MB/s
Collecting python-dotenv
  Downloading python_dotenv-0.21.0-py3-none-any.whl (18 kB)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\bhaja\dev\selenium_example\venv\lib\site-packages (from requests->webdriver_manager) (1.26.12)
Collecting charset-normalizer<3,>=2
  Using cached charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\bhaja\dev\selenium_example\venv\lib\site-packages (from requests->webdriver_manager) (2022.9.24)
Requirement already satisfied: idna<4,>=2.5 in c:\users\bhaja\dev\selenium_example\venv\lib\site-packages (from requests->webdriver_manager) (3.4)
Collecting colorama
  Using cached colorama-0.4.5-py2.py3-none-any.whl (16 kB)
Installing collected packages: colorama, charset-normalizer, tqdm, requests, python-dotenv, webdriver-manager
Successfully installed charset-normalizer-2.1.1 colorama-0.4.5 python-dotenv-0.21.0 requests-2.28.1 tqdm-4.64.1 webdriver-manager-3.8.3
WARNING: You are using pip version 21.2.3; however, version 22.2.2 is available.
You should consider upgrading via the 'C:\Users\bhaja\dev\selenium_example\venv\Scripts\python.exe -m pip install --upgrade pip' command.


(venv) PS C:\Users\bhaja\dev\selenium_example> python
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> from webdriver_manager.chrome import ChromeDriverManager
>>> from selenium.webdriver.common.keys import Keys
>>> from bs4 import BeautifulSoup
>>> from selenium import webdriver
>>> driver = webdriver.Chrome(ChromeDriverManager().install())
(browser opens but getting errors so just trying code now)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home



PS C:\Users\bhaja\dev\selenium_example> choco install chromedriver
Chocolatey v0.11.3
Installing the following packages:
chromedriver
By installing, you accept licenses for the packages.
Progress: Downloading chromedriver 106.0.5249.610... 100%

chromedriver v106.0.5249.610 [Approved]
chromedriver package files install completed. Performing other installation steps.
The package chromedriver wants to run 'chocolateyinstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y

Downloading packageName
  from 'https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip'
Progress: 100% - Completed download of C:\Users\bhaja\AppData\Local\Temp\chocolatey\chromedriver\106.0.5249.610\chromedriver_win32.zip (6.29 MB).
Download of chromedriver_win32.zip (6.29 MB) completed.


NEW ERROR:
    (venv) PS C:\Users\bhaja\dev\selenium_example> & c:/Users/bhaja/dev/selenium_example/venv/Scripts/python.exe c:/Users/bhaja/dev/selenium_example/crawler.py
c:\Users\bhaja\dev\selenium_example\crawler.py:18: DeprecationWarning: use options instead of chrome_options
  driver = webdriver.Chrome(chrome_options=options)

DevTools listening on ws://127.0.0.1:56483/devtools/browser/7fcf4c2d-810a-4c57-b6c5-166371b5dd8b
Traceback (most recent call last):
  File "c:\Users\bhaja\dev\selenium_example\crawler.py", line 18, in <module>
    driver = webdriver.Chrome(chrome_options=options)selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 106
Current browser version is 105.0.5195.127 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe