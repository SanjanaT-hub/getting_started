import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv

url="https://www.dhanbank.com/interest-rates/"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table30")[1]

#table=soup.find("table",{'class': 'rates-table-main'})

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]

for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)



headings=LIST_OF_INTEREST_RATES[0]
final_rates=LIST_OF_INTEREST_RATES[1:]
'''print(headings)
print(final_rates)'''

x=0

for i in final_rates:
    #print(i)
    if x>=6:
        senior_rate=float(i[1])+0.50
        i.append(senior_rate)
        print(senior_rate)
        x+=1
    else:
        senior_rate=float(i[1])
        i.append(senior_rate)
        x+=1

        


# to remove \xa0 characters
final_rates = [[cell.replace('\xa0', '') if isinstance(cell, str) else cell for cell in row] for row in final_rates]
print(final_rates)



rates=[]
for i in final_rates:
    x=['Dhanlaxmi Bank']
    x.extend(i)
        #x.extend(i[1:])  # Add tenure and rates
    x.insert(3, '')  # Placeholder for annualised_gen_rate
    x.insert(4, '')

    x.insert(5, '')  # Placeholder for annualised_sr_rate
    x.insert(6, '')
    x.insert(7, '')  # Placeholder for annualised_super_sr_rate
    x.append(30000000)
    rates.append(x)
print(rates)
    

int_rate_df = pd.DataFrame(rates, columns=[
    'bank_name', 'tenure', 'gen_rate', 'annualised_gen_rates', 
    'sr_rate', 'annualised_sr_rates', 'super_sr_rates', 
    'annualised_super_sr_rates', 'threshold_amt'
])
pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv('Interest_Rates(dhanlaxmi_bank).csv',mode='a',header='False',index=False)


    







    
