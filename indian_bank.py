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




url="https://www.indianbank.in/departments/deposit-rates/"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="")
#table=soup.find("table",{'class': 'rates-table-main'})


rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=['Indian Bank']
    row.extend([tr.text for tr in data])
    row.append(30000000)
    LIST_OF_INTEREST_RATES.append(row)


final_rates = LIST_OF_INTEREST_RATES[2:]

print(final_rates)


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)







