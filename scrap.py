from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
c=1
url = "https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print("\n\nNEWS:: on ",datetime.now(),"\n")
print("------------------------------------------------------------------------")
for name_box in soup.find_all('a', attrs={'class': 'nuEeue hzdq5d ME7ew'}):
	if c<=10:
		name = name_box.text.strip()
		print(name,"\n")
		c+=1


#price_box = soup.find('div', attrs={'class':'price'})
#price = price_box.text
#print(price)
#with open('index.csv', 'a') as csv_file:
#	writer = csv.writer(csv_file)
#	writer.writerow([name, price, datetime.now()])