import csv 
import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)


url="https://bankofmaharashtra.in/domestic-term-deposits"
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
    row=[tr.text for tr in data]
 
    LIST_OF_INTEREST_RATES.append(row)



headings =["Tenure","(% per annum )"]
final_rates = LIST_OF_INTEREST_RATES[2:]
final_rates = [[item.replace('\xa0', '').replace('\n', '').strip() for item in sublist] for sublist in final_rates]


result = []
for row in LIST_OF_INTEREST_RATES[6:]:
    # Keep only the first two elements of each row
    filtered_row = row[:2]
    result.append(filtered_row)

for i in result:
    i[1]=str(i[1]) + '%'

print(result)
final_rates=[]
for i in result:
    print(i)
    
    row=['Bank of Maharashtra']
    row.extend(i)
    row.append('') # annualised general rate
    row.append('') # senior rate
    row.append('') # senior annualised rate
    row.append('') # super senior
    row.append('') # annualised super senior
    row.append(30000000)
    final_rates.append(row)
print(final_rates)
    

int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])


pd.set_option('display.max_columns',None)
print(int_rate_df)

file_name='Interest_rate_' + date1 + '.csv'
print(file_name)
int_rate_df.to_csv(file_name,mode='a',header=False,index=False)







