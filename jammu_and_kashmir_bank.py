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



url="https://www.jkbank.com/others/common/intrates.php"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table-bordered table-condensed table-hover")
#table=soup.find("table",{'class': 'rates-table-main'})
if len(table)>1:
    table=table[1]

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]


for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)



# Create a new list with only the first and fourth elements
new_list = [[sublist[0], sublist[3]] for sublist in LIST_OF_INTEREST_RATES]



for i in new_list:

    senior_rate=float(i[1][:4])+0.50
    senior_rate=str(senior_rate)+'%'
    i.append(senior_rate)



# Print the new list
print(new_list)

final_rates=[]
for i in new_list:
    x=['Jammu and Kashmir Bank']
    x.extend(i)
    x.insert(3, '')
    x.insert(5, '')
    x.insert(6, '')
    x.insert(7, '') 
    x.append(30000000)
    final_rates.append(x)
print(final_rates)
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])


pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv(file_name,mode='a',header='False',index=False)

