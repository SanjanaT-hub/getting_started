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



url="https://www.sc.com/in/deposits/interest-rates/#sc-lb-module-fee-and-rate-5"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="")
table=table[3]

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]

for i in rows[3:41]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

LIST_OF_INTEREST_RATES= [sublist[:2] for sublist in LIST_OF_INTEREST_RATES]



print("LIST OF INTEREST RATES:", LIST_OF_INTEREST_RATES)

final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['Standard Chartered Bank']
    x.extend(i)
    x.insert(4, '')
    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(20000000)
    final_rates.append(x)
print(final_rates)
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)



