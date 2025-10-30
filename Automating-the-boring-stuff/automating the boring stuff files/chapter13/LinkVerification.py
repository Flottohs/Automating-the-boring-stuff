#Write a program that, given the URL of a web page, will find every <a> link on the page and test whether the linked URL results in a “404 Not Found” status code. The program should print out any broken links.

import requests
from bs4 import BeautifulSoup


def linkchecker(link):
    
    
    
    try:
        res= requests.get(link)
        status = res.raise_for_status()
        print(status)
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        
    soup = BeautifulSoup(res.text,'html parser')    
    for link in soup.findall('a'):  
        url = link.get('href')
        try:
            res = requests.get(url)
            res.raise_for_status()
        except Exception as exc:
            print(f"Broken link: {url} - {exc}")
        
    
    
    
    
    
print("input link")
link = input()
linkchecker(link)