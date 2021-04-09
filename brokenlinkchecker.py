#control + shift
#How-to: https://dev.to/arvindmehairjan/build-a-web-crawler-to-check-for-broken-links-with-python-beautifulsoup-39mg
# Import libraries
from bs4 import BeautifulSoup, SoupStrainer
import requests

# Prompt user to enter the URL
url = input("Enter your url: ")

# Make a request to get the URL
page = requests.get(url)

# Get the response code of given URL
response_code = str(page.status_code)

# Display the text of the URL in str
data = page.text

# Use BeautifulSoup to use the built-in methods
soup = BeautifulSoup(data)

# Iterate over all links on the given URL with the response code next to it
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")

# 4-8-2021. Having trouble with the last step. It says to:

# Now run the script by typing python verify_response_code.py in your terminal. 
#You are asked to enter an URL. Enter the given the URL and press enter. 
#If things are going well, you should receive an output like this below.

#### #### #### #### #### #### 
#### #### PROBLEMS #### #### 
#### #### #### #### #### #### 

#however, when I try running the script by typing: 
#brokenlinkchecker.py 
#into my terminal, it doesn't run. instead I get this:

#(base) Kristens-MacBook-Air:~ kcchua$ cd Documents/GitHub/crispy-winner
#(base) Kristens-MacBook-Air:crispy-winner kcchua$ pwd
#/Users/kcchua/Documents/GitHub/crispy-winner
#(base) Kristens-MacBook-Air:crispy-winner kcchua$ brokenlinkchecker.py
#-bash: brokenlinkchecker.py: command not found

#things I want to improve on:
#1) Edit this broken link checker so that it reads links from a file
#2) 