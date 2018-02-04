import requests
import sys, threading
from bs4 import BeautifulSoup, SoupStrainer
import lxml

originalPrice =""
discountPrice =""
medication ="xanax"
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
    strainer = SoupStrainer('div', { 'class' : ['pricerow-store', 'pricerow-drugprice', 'store-name']})
    soup = BeautifulSoup(plainText, "lxml", parse_only=strainer)
    # originalPrice = soup.find(class_ ="est-price").text
    # discountPrice = soup.find(class_ ="drug-price").text
    # store=soup.find(class_ ="store-name").text

    #for result in soup.findAll(class_ ="store-name", class_ ="est-price"):
    for result in soup.findAll(class_ =['store-name', 'drug-price']):
        print(result.text)

    # print(originalPrice)
    # print(discountPrice)
    # print(store)


if __name__ == "__main__":
    goodrx = crawl_pages()
