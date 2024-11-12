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

#5 CRORES
url="https://nesfb.com/Interest_Rates"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="table table-bordered")

headers=["Tenure","General Interest Rate","Senior Interest Rate"]

print(headers)

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[3:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)


LIST_OF_INTEREST_RATES=[sublist[:3] + sublist[5:] for sublist in LIST_OF_INTEREST_RATES]



final_rates = []

for i in LIST_OF_INTEREST_RATES:
    x = ['IndusInd Bank']
    x.extend(i)  # Tenure, gen_rate, sr_rate
    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(50000000)  # Threshold amount
    final_rates.append(x)

print(final_rates)

int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)







