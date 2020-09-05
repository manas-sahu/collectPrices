#Flipkart Zebronics Max Pro price
flipkartPage = requests.get('https://www.flipkart.com/zebronics-max-pro-mechanical-usb-wired-keyboard-gaming/p/itmf3v6n4uaxsnaa', headers=HEADERS)
flipkartSoup = BeautifulSoup(flipkartPage.content, features="lxml")
flipkartPrice = flipkartSoup.find('div', class_="_1vC4OE _3qQ9m1").get_text().replace(u'₹', u'').strip()
flipkartAvailability = flipkartSoup.find('div', class_="_9-sL7L").get_text().strip()
flipkartTittle = flipkartSoup.find('span', class_="_35KyD6").get_text().replace(u'\xa0', u' ')
print ('Flipkart ' + flipkartTittle + '  ==>  ' + flipkartPrice + '   ' + flipkartAvailability)

#Prime abgb ASUS TUF GAMING X570-PLUS
primeAbgbPage = requests.get('https://www.primeabgb.com/online-price-reviews-india/asus-tuf-gaming-x570-plus-amd-x570-wi-fi-atx-gaming-motherboard/', headers=HEADERS)
primeAbgbSoup = BeautifulSoup(primeAbgbPage.content, features="lxml")
primeAbgbPrice = primeAbgbSoup.find_all('span', class_="woocommerce-Price-amount amount")[2].get_text()
primeAbgbTittle = primeAbgbSoup.find('h1', class_="product_title entry-title").get_text().strip()
print ('prime abgb ' + primeAbgbTittle + '  ==>  ' + primeAbgbPrice)

#Amazon Zebronics Max Pro price
amazonPage = requests.get('https://www.amazon.in/Zebronics-Mechanical-Wired-Keyboard-Black/dp/B078NWJ6VM/ref=sr_1_3?dchild=1&keywords=zebronics+max+pro&qid=1599161805&sr=8-3', headers=HEADERS)
amazonSoup = BeautifulSoup(amazonPage.content, features="lxml")
amazonPrice = amazonSoup.find(id='priceblock_ourprice').get_text().replace(u'₹', u'').strip()
amazonTittle = amazonSoup.find(id='productTitle').get_text().strip()
amazonAvailability = amazonSoup.find(id='availability').get_text().strip()
print ('Amazon ' + amazonTittle + '  ==>  ' + amazonPrice + '   ' + amazonAvailability)
# addPriceToJSON(website, tittle, price, availability)