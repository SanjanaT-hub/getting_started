import csv 
import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
from datetime import date




url="https://bankofindia.co.in/interest-rate/rupee-term-deposit-rate"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="table")

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]

row_count=0
for i in rows[1:]:  # Skipping heading
    data = i.find_all("td")
    # Extract the text from the first two columns only
    row=['Bank of India']
    row.extend([ tr.text for tr in data[:2]])
    print(row)
    row[2]=str(row[2]) + '%'
    print(row)
    row.append('') # general annualised rate
    if row_count<=4:
        row.append(str(row[2][:3]) + '%')
        row.append('')
        row.append(str(row[2][:3]) + '%')
        row.append('')
    else:
        #print("printing",row[2])
        row.append(str(float(row[2][:3])+0.50) + '%')
        row.append('')
        row.append(str(float(row[2][:3])+0.65) + '%')
        row.append('')
    row.append(30000000)
    row_count+=1
    LIST_OF_INTEREST_RATES.append(row)
           
print( LIST_OF_INTEREST_RATES)
today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
int_rate_df=pd.DataFrame(LIST_OF_INTEREST_RATES,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])


pd.set_option('display.max_columns',None)
print(int_rate_df)


file_name='Interest_rate_' + date1 + '.csv'
print(file_name)
int_rate_df.to_csv(file_name,mode='w',header=True,index=False)





















