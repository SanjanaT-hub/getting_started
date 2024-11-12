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

url="https://www.tmb.in/pages/Deposit-Interest-Rates"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="")

table=table[1]

headers=["Tenure","General Public Interest Rate","Senior Citizens Interest Rate"]

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

LIST_OF_INTEREST_RATES = [[item.replace('\n', '').replace('\xa0', '') for item in sublist] for sublist in LIST_OF_INTEREST_RATES]


print(headers)
print(LIST_OF_INTEREST_RATES)


final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['Tamilnad Mercantile Bank']
        # Append '%' to the rates
    gen_rate = i[1].strip() + '%' if i[1] else ''
    sr_rate = i[2].strip() + '%' if i[2] else ''
    x.extend([i[0], gen_rate, sr_rate]) 

    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(30000000)
    final_rates.append(x)
print(final_rates)
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)

