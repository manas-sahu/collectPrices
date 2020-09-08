import requests
from bs4 import BeautifulSoup
import json
from iteration_utilities import unique_everseen
from datetime import datetime
# https://towardsdatascience.com/scraping-multiple-amazon-stores-with-python-5eab811453a8
# https://www.youtube.com/watch?v=lwmymf-7NJU
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
#print Data in console
def printData(website, tittle, price, availability):
    print (website +'  '+tittle + '  ==>  ' + str(price) + '   ' + availability)

# Creating JSON file
# function to add to JSON 
def write_json(data, filename): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

# To keep only unique values
# def keepUniqueValue():
#     with open('backupData.json') as json_file: 
#         data = json.load(json_file) 
#         temp = list(unique_everseen(data['scrappedPrice']))
#         write_json(temp, 'data.json')
        
def addPriceToJSON(website, tittle, price, availability, url):      
    with open('data.json') as json_file: 
        data = json.load(json_file) 
        temp = data
        ts = datetime.now().strftime("%x")
        # python object to be appended 
        y = {
            "Website": website,
            "product_name": tittle, 
            "product_url": url,
            "product_price": price, 
            "product_availablity": availability,
            "time": ts
            }
        guest_flag = 0
        for i in range (0, len(temp)):
            if(temp[i]['Website'] == y['Website'] and 
            temp[i]['product_name'] == y['product_name'] and 
            temp[i]['product_url'] == y['product_url'] and 
            temp[i]['product_price'] == y['product_price'] and 
            temp[i]['product_availablity'] == y['product_availablity'] and 
            temp[i]['time'] == y['time']):
                guest_flag = 1   
        # appending data to emp_details 
        if(guest_flag == 0):
            temp.append(y) 
            write_json(data, 'data.json')
            #keepUniqueValue()

# Amazon
def loadAmazon(data):
    page = requests.get(data["url"], headers=HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="lxml")
        if soup:
            getPrice = soup.find(id='priceblock_ourprice')
            if getPrice:
                price = int(getPrice.get_text().replace(u'₹', u'').replace(u',', u'').strip().split('.')[0])
            else :
                price = 0
            tittle = soup.find(id='productTitle').get_text().strip()
            availability = soup.find(id='availability').get_text().replace(u'\n', u'').strip()
            addPriceToJSON(data["website"], tittle, price, availability, data["url"])
            printData(data["website"], tittle, price, availability)

# Flipkart
def loadFlipkart(data):
    page = requests.get(data["url"], headers=HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="lxml")
        if soup:
            getPrice = soup.find('div', class_="_1vC4OE _3qQ9m1")
            if getPrice:
                price = int(getPrice.get_text().replace(u'₹', u'').replace(u',', u'').strip())
            else :
                price = 0
            tittle = soup.find('span', class_="_35KyD6").get_text().replace(u'\xa0', u' ')
            availability = soup.find('div', class_="_9-sL7L").get_text().strip()
            addPriceToJSON(data["website"], tittle, price, availability, data["url"])
            printData(data["website"], tittle, price, availability)

# Prime abgb
def loadPrimeAbgb(data):
    page = requests.get(data["url"], headers=HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="lxml")
        if soup:
            getPrice = soup.find_all('span', class_="woocommerce-Price-amount amount")[2]
            if getPrice:
                price = int(getPrice.get_text().replace(u'₹', u'').replace(u',', u'').strip())
            else :
                price = 0
            tittle = soup.find('h1', class_="product_title entry-title").get_text().strip()
            getAvailability = soup.find('p', class_="stock out-of-stock")
            if getAvailability:
                availability = getAvailability.get_text().strip()
            else :
                availability = "In Stock"
            addPriceToJSON(data["website"], tittle, price, availability, data["url"])
            printData(data["website"], tittle, price, availability)

# MD Computers
def loadMdComputers(data):
    page = requests.get(data["url"], headers=HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, features="lxml")
        if soup:
            getPrice = soup.find('span', class_="price-new")
            if getPrice:
                price = int(getPrice.get_text().replace(u'₹', u'').replace(u',', u'').strip())
            else :
                price = 0
            tittle = soup.find('div', class_="title-product").get_text().strip()
            availability = soup.find('div', class_="stock").get_text().replace(u'Availability:  ', u'').strip()
            addPriceToJSON(data["website"], tittle, price, availability, data["url"])
            printData(data["website"], tittle, price, availability)
  

json_data_file = open('productList.json')
list_data = json.load(json_data_file)

for item in list_data['itemslist']:
    url = item["url"]
    website = item["website"]
    if website == "amazon":
        loadAmazon(item)
    if website == "flipkart":
        loadFlipkart(item)
    if website == "primeabgb":
        loadPrimeAbgb(item)
    if website == "mdcomputers":
        loadMdComputers(item)