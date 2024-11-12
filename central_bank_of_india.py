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




url="https://www.centralbankofindia.co.in/en/interest-rates-on-deposit"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",{'class': "Table"})

if len(table) > 1:
    table = table[1]
'''headers=table.find_all("th")

print(headers)'''

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]
print(rows)

for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=['Central Bank of India']
    row.extend([tr.text for tr in data])
    row.extend(['','',30000000])
    LIST_OF_INTEREST_RATES.append(row)

LIST_OF_INTEREST_RATES=LIST_OF_INTEREST_RATES[2:]
final_rates=[[cell.replace('\n', '').strip() if isinstance(cell, str) else cell for cell in row] for row in LIST_OF_INTEREST_RATES]


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)
































