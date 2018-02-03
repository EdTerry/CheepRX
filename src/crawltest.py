import requests
import sys, threading
from bs4 import BeautifulSoup, SoupStrainer

# WellRX Crawler

medName = "adderall"
userZip = "33018"

getStoreName = ""
getStoreAddr = ""
getDrugPrice = ""

def crawl_WellRx(medName):
    #url = "https://www.wellrx.com/prescriptions/"+str(medName).lower()+"/?address="+str(userZip)

    url="https://goodrx.com/"+str(medName).lower()+"?drug-name="+str(medName).lower()
    print(url)

    source_code = requests.get(url)
    plain_text = source_code.text
    strainer = SoupStrainer('div', {'class': 'drug-panel'})
    soup = BeautifulSoup(plain_text, "lxml", parse_only=strainer)

    getStoreInfo = soup.find(class_='drug-panel').string

    print(getStoreInfo)

if __name__ == "__main__":
    medName = "ADDERALL"
    crawl_WellRx(medName)
