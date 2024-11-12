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


url="https://punjabandsindbank.co.in/content/interestdom"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table")

if len(table) > 1:
    table = table[1]

rows=table.find_all("tr")
print(rows)
LIST_OF_INTEREST_RATES=[]
for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=['Punjab and Sind Bank']
    row.extend([tr.text for tr in data])
    row[2]=str(row[2][:3])+'%'
    row.append('') # annualised general rate
    LIST_OF_INTEREST_RATES.append(row)
#print(LIST_OF_INTEREST_RATES)

headings=LIST_OF_INTEREST_RATES[0:1]
final_rates=LIST_OF_INTEREST_RATES[1:]

#print(headings)
#print(final_rates)
x=0

for i in final_rates:
    if x>=7:
        i.append(str(float(i[2][:3])+float(0.50))[:3] + '%')
        i.append('') # annualised senior rate
        i.append(str(float(i[2][:3])+float(0.65))[:3] + '%')
        i.append('') # annualised super senior rates
        i.append(30000000)
        #print(y)
    else:
        i.append('')
        i.append('')
        i.append('')
        i.append('')
        i.append(30000000)
    x+=1
print()
print("###################################")
print("RATES WITH SENIOR CITIZENS",final_rates)


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)





        
