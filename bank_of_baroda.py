import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv

url="https://www.bankofbaroda.in/interest-rate-and-service-charges/deposits-interest-rates"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")
print(soup)

table=soup.find("table",class_="responsiveTable tableData")
#table=soup.find("table",attrs={'class': 'responsiveTable tableData'})


headers=table.find_all("th")
print(headers)
titles=[]
for i in headers:
    title=i.text
    titles.append(title)
rows=table.find_all("tr")

