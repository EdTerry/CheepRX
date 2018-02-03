import requests
import sys, threading
from bs4 import BeautifulSoup, SoupStrainer
import lxml

originalPrice =""
discountPrice =""
medication ="adderall"
store =""
distance =""
url=""


#class crawl_goodrx():    

def crawl_pages():
    global originalPrice
    global discountPrice
    global store
    global url

    url = "https://www.goodrx.com/" + medication + "?drug-name=" + medication
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    strainer = SoupStrainer('div', { 'event-id' : 'priceRow'})
    soup = BeautifulSoup(plainText, "lxml", parse_only=strainer)
    originalPrice = soup.find(class_ ="est-price").string
    discountPrice = soup.find(class_ ="drug-price")
    store=soup.find(class_ ="store-name")

    print(originalPrice)
    print(discountPrice)
    print(store)
        

if _name_ == "_main_":
    goodrx = crawl_pages()