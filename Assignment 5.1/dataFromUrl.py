from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd

#1
url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'
raw_html = requests.get(url)
data = BeautifulSoup(raw_html.content,'html5lib')

mobile_name = data.find_all('div',attrs={'class':'_3wU53n'})
mobile_price = data.find_all('div',attrs={'class':'_1vC4OE _2rQ-NK'})
ModelName,ModelPrice = [],[]
for i in mobile_name:
    ModelName.append(i.text)
for j in mobile_price:
    ModelPrice.append(j.text)
indax=len(ModelName)
df = pd.DataFrame({'ModelName':ModelName,'ModelPrice':ModelPrice},index=range(indax))
print(df)

df.to_csv('flipkart.csv')


#2
from os.path import basename

url = 'https://www.passiton.com/inspirational-quotes'
raw_html = requests.get(url)
data = BeautifulSoup(raw_html.content,'html5lib')

quotes = data.find('div',attrs={'id':'all_quotes'})
links=[]

for quote in quotes.find_all('div',attrs={'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    links.append(quote.img['src'].split('?')[0])

for link in links:
    with open(f'F:\sem 5\Python\Programs\Assignment 5.1\Quotes\{basename(link)}','wb') as file:
        file.write(requests.get(link).content)
