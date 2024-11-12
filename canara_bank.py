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




url="https://canarabank.com/pages/deposit-interest-rates"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")

#table=soup.find("table",class_="table table-striped table-borderd table-hover")
table=soup.find_all("table",{'class': "table table-striped table-borderd table-hover"})

if len(table) > 1:
    table = table[1]
'''headers=table.find_all("th")

print(headers)'''

rows=table.find_all("tr")
rows=rows[6:]
print(rows)
print("###########################")
LIST_OF_INTEREST_RATES=[]
###############################################################
#ERROR IN TABLE: SHOWING EXTRA LINES
################################################################
for i in rows[:12]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=[]
    row.extend([tr.text for tr in data])

    LIST_OF_INTEREST_RATES.append(row)



cleaned_data = LIST_OF_INTEREST_RATES[:10]



# Print the result
cleaned_data = [row[:5] for row in cleaned_data]



final_rates= [[cell.strip() for cell in sublist] for sublist in cleaned_data]


final_rate=[]
for i in final_rates:
    x = ['Canara Bank']
    
    # Add '%' to each appropriate element if missing
    for j in range(1, 5):  # Check indices 1 to 4
        if '%' not in i[j]:
            i[j] += '%'
    
    x.extend(i)
    x.extend(['', ''])  # Super senior rates
    x.append(30000000)
    final_rate.append(x)

final_rates = [
    [str(cell).replace('\r\n', '').strip() for cell in row] for row in final_rate # not working
]

print(final_rates)

int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)





