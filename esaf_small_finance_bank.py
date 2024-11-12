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



url="https://www.esafbank.com/interest-rates/"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="")

table1=table[2]
headers=['Period','Normal Rate (%)', 'Rate for Senior Citizens (%)']

print(headers)


rows=table1.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[2:]:  #skipping heading

    data=i.find_all("td")
    row=['ESAF Bank']
    row.extend([tr.text for tr in data])
    row.insert(3, '')
    row.insert(5, '')
    row.insert(6, '')
    row.insert(7, '') 
    row.append(30000000)
    LIST_OF_INTEREST_RATES.append(row)


print("LIST OF INTEREST RATES:", LIST_OF_INTEREST_RATES)




int_rate_df=pd.DataFrame(LIST_OF_INTEREST_RATES,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)










