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


url="https://www.idbibank.in/interest-rates.aspx"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table table-border-light")

table=table[3]

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[2:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

final_rates=LIST_OF_INTEREST_RATES[1:]
final_rates = [
    [
        item.replace('\r\n', '').replace('\xa0', '').strip()  # Remove unwanted characters and extra spaces
        for item in sublist if item.strip()  # Remove empty items after stripping
    ]
    for sublist in final_rates
    if sublist and 'Tax Saving FD' not in sublist  # Remove empty lists and specific sublist
]

final_rates=final_rates[1:]


final_rate=[]
for i in final_rates:
    x=['IDBI Bank']
    # Append '%' to the rates
    gen_rate = i[1].strip() + '%' if i[1] else ''
    sr_rate = i[2].strip() + '%' if i[2] else ''
    x.extend([i[0], gen_rate, sr_rate])
    
    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(30000000)
    final_rate.append(x)
print(final_rate)
    



int_rate_df=pd.DataFrame(final_rate,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)







