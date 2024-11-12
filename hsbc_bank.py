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


url="https://www.hsbc.co.in/accounts/products/fixed-deposits/"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="desktop")

headers=table.find_all("th")
#print(headers)
titles=[]
for i in headers:
    title=i.text
    titles.append(title)

final_titles=titles[0:3]

tenures=titles[3:]
#print(tenures)



rows=table.find_all("tr")
#print(rows)

LIST_OF_INTEREST_RATES=[]

for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)
    
final_rates=[]
#################################################################################



# Initialize the final list
final_rates = []

# Iterate over tenure and interest_rates simultaneously
for i in range(len(tenures)):
    # Create a nested list with [tenure, regular_interest_rate, senior_interest_rate]
    combined = [tenures[i], LIST_OF_INTEREST_RATES[i][0], LIST_OF_INTEREST_RATES[i][1]]
    # Append the combined list to final_list
    final_rates.append(combined)

# Print the final result




###############################################################################
print("printing")
print(final_rates)


final_rate=[]
for i in final_rates:
    x=['HSBC Bank']
    gen_rate = i[1].strip() + '%' if i[1] else ''
    sr_rate = i[2].strip() + '%' if i[2] else ''
    x.extend([i[0], gen_rate, sr_rate])  # Tenure, gen_rate, sr_rate
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







