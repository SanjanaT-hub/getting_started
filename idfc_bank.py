import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)


url="https://www.idfcfirstbank.com/personal-banking/deposits/fixed-deposit/fd-interest-rates"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="test formtable")
#table=soup.find("table",{'class': 'rates-table-main'})
if len(table)>1:
    table1=table[0]
    table2=table[1]

rows1=table1.find_all("tr")
LIST_OF_INTEREST_RATES=[]

for i in rows1:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)


rows2=table2.find_all("tr")
for i in rows2[1:]:  #skipping heading

    data=i.find_all("td")
    row=[tr.text for tr in data]
    snr_rate=float(row[1][:4])+0.50
    row.append(str(snr_rate)+'%')
    LIST_OF_INTEREST_RATES.append(row)

 
headings=LIST_OF_INTEREST_RATES[0]
LIST_OF_INTEREST_RATES=LIST_OF_INTEREST_RATES[1:]

final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['IDFC Bank']
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




