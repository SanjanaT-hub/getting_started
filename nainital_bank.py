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
 

url="https://www.nainitalbank.co.in/english/interest_rate.aspx"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table table-bordered")

table=table[1]

headers=table.find_all("th")

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]



for i in rows[2:17]:  #skipping heading

    data=i.find_all("td")
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)


LIST_OF_INTEREST_RATES = [[item.strip() for item in sublist] for sublist in LIST_OF_INTEREST_RATES]


for i in LIST_OF_INTEREST_RATES[:16]:
    if i[0]=='Naini    Tax Saver Scheme*':
        i.append('')
        i.append('')
    else:
        senior_rate=float(i[1][:4])+0.50
        senior_rate=str(senior_rate)+'%'
        super_senior_rate=float(i[1][:4])+0.60
        super_senior_rate=str(super_senior_rate)+'%'
        i.append(senior_rate)
        i.append(super_senior_rate)
#print(LIST_OF_INTEREST_RATES)
print("#############")

final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['Nainital Bank']
    x.extend(i)
    x.insert(3,'')
    x.insert(5,'')
    x.insert(7,'')
    x.append(20000000)
    print(x)
    final_rates.append(x)
print(final_rates)
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv(file_name,mode='a',header='False',index=False)


