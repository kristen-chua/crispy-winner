#control + shift
#How-to: https://dev.to/arvindmehairjan/build-a-web-crawler-to-check-for-broken-links-with-python-beautifulsoup-39mg

### Step 0: Make sure I'm in the right directory
## pwd = print working directory
## cd = change directory i.e. cd /Users/kcchua/Documents/GitHub/crispywinner
## related documentation: https://stackoverflow.com/questions/34109771/python-101-cant-open-file-no-such-file-or-directory


#check which version of Python I'm using
import sys
print(sys.version) # 3.9.4 
print(sys.path) # /Users/kcchua/Documents/GitHub/crispy-winner. 
#Turns out I needed to update to python 3. Updated to 3.9.4 as of April 12,2021 
#how to change python version I'm using: 
#https://medium.com/swlh/setting-your-python-version-in-sublime-text-8e8a305e6701#:~:text=Find%20your%20Python%20path&text=Change%20the%20%E2%80%9Cshell_cmd%E2%80%9D%3A%20%E2%80%9C,the%20correct%20version%20being%20run.
# then I needed to install pip? Run 'python get-pip.py' in the terminal. 2 This will install or upgrade pip.
# Test to see if it is working by typing 'python3 -m pip --version' in the Terminal 
# figured out that you can't just run pip in Python code, it needs to be run in Terminal/ Command Line
# resource: https://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip


## Import libraries
# Import BeautifulSoup4 by running this in the Terminal:
# pip install beautifulsoup4
from bs4 import BeautifulSoup, SoupStrainer
# Import requests by running $ pip install requests in Terminal
#https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
import requests


## This is where the action begins
## Now run the script by typing 'python brokenlinkchecker.py' in your terminal. 
## You are asked to enter an URL. Enter the given the URL and press enter. 
#example URL: https://www.marvel.com/404 , https://www.creativebloq.com/web-design/best-404-pages-812505

# Prompt user to enter the URL
url = input("Enter your url: ")

# Make a request to get the URL
page = requests.get(url)

# Get the response code of given URL
response_code = str(page.status_code)

# Display the text of the URL in str
data = page.text

# Use BeautifulSoup to use the built-in methods
soup = BeautifulSoup(data, features="html.parser")

# Iterate over all links on the given URL with the response code next to it
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")
# 4-8-2021. Having trouble with the last step. It says to:
# -something something something-

# to see when brokenlinkchecker.py was last saved, type in terminal:
#stat brokenlinkchecker.py
#If things are going well, you should receive an output like this below.

#### #### #### #### #### #### 
#### #### PROBLEMS #### #### 
#### #### #### #### #### #### 


#
#things I want to improve on:
#1) Edit this broken link checker so that it reads links from a file
#2) 