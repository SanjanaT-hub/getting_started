import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv

url="https://www.csb.co.in/interest-rates"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table")
print(soup.prettify())
#table=soup.find("table",{'class': 'rates-table-main'})
print(len(table))
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
    x=['CSB Bank']
    x.extend(i)
    x.append(30000000)
    final_rates.append(x)
print(final_rates)
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','sr_rate','threshold_amt'])


pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv('Interest_Rates(HDFC_bank).csv',mode='a',header='False',index=False)












