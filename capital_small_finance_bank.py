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




#PUT IN FUNCTION
url="https://www.capitalbank.co.in/interest-rates/callable-domestic-term-deposit"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find_all("table",class_="table")

table1=table[0]
table2=table[1]

rows=table1.find_all("tr")
RATES=[]


for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    RATES.append(row)

RATES = [item for item in RATES if item != ['Special category']]

print(RATES)
##########

rows=table2.find_all("tr")
SENIOR_RATES=[]


for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    SENIOR_RATES.append(row)
print(RATES)

for rate in RATES:
    period = rate[0]
    # Find the matching senior rate
    senior_rate_found = False
    for senior_rate in SENIOR_RATES:
        if senior_rate[0] == period:
            rate.append(senior_rate[1])
            senior_rate_found = True
            break
    if not senior_rate_found:
        rate.append('NA')  # Append 'NA' if no matching period is found in SENIOR_RATES



############################TAX SAVER RATES
url="https://www.capitalbank.co.in/interest-rates/tax-saver-fixed-deposit"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="table")

rows=table.find_all("tr")
tax_saver=[]


for i in rows[1:2]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    tax_saver.append(row)

seniorrate=float(tax_saver[0][1][:4])+0.50
seniorrate=str(seniorrate)+'%'
tax_saver[0].append(seniorrate)


RATES.append(tax_saver[0])
print(RATES)


final_rates=[]
for i in RATES:
    x=['Capital Small Finance Bank']
    x.extend(i)
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



