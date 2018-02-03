import requests
import sys, threading
from bs4 import BeautifulSoup, SoupStrainer
import lxml

originalPrice =""
discountPrice =[]
medication ="adderall"
store =[]
distance =""
url=""
keys=""


#class crawl_goodrx():    
    

def crawl_pages():
    global originalPrice
    global discountPrice
    global store
    global url
    global keys

    url = "https://www.goodrx.com/" + medication + "?drug-name=" + medication
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    strainer = SoupStrainer('div', {'class': 'store-name '})
    soup = BeautifulSoup(plainText, "lxml", parse_only=strainer)    
    strainer2 = SoupStrainer('div', {'class': 'pricerow-drugprice'})
    soup2 = BeautifulSoup(plainText, "lxml", parse_only=strainer2)

    for x in soup.find_all(class_={'store-name'}):
        store.append(x.text.strip())

    for x in soup2.find_all(class_={'drug-price'}):
        discountPrice.append(float(x.text.strip('$')))

    dict_ = {}

    for storeName, dPrice in zip(store, discountPrice):
        dict_[storeName] = dPrice

    for x in dict_:
        print("{} {}".format(x, dict_[x]))

if __name__ == "__main__":
    goodrx = crawl_pages()