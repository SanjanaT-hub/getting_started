import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv
from datetime import date


today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name='Interest_rate_' + date1 + '.csv'
print(file_name)


url="https://www.hdfcbank.com/personal/save/deposits/fixed-deposit-interest-rate"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="rates-table-main")
#table=soup.find("table",{'class': 'rates-table-main'})

headers=table.find_all("th")

#print(headers)
titles=[]
for i in headers:
    title=i.text
    titles.append(title)


for i in titles:
    if i=="< 3 Crore":
       titles.remove(i)

titles[1]=titles[2]
titles[2]=titles[3]
x=titles.pop()
print("LIST OF TITLES:")
print(titles)
print()
print()

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]

for i in rows[2:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)
print(LIST_OF_INTEREST_RATES)

final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['HDFC Bank']
    x.extend(i)
    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(30000000)
    final_rates.append(x)
print(final_rates)
    

int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv(file_name,mode='a',header='False',index=False)












