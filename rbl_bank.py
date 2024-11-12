import requests  # fetches data from webpage
from bs4 import BeautifulSoup  # extracts data we need
import pandas as pd  # to store data as csv or excel format
from datetime import date


today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name='Interest_rate_' + date1 + '.csv'
print(file_name)




url = "https://www.rblbank.com/interest-rates?srsltid=AfmBOopSpSNYKdXDZfY6oCv6TyicvNtbNS4M0E9XdR8L4JfM3toO-hTu"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find_all("table", class_="")
table = table[1]

rows = table.find_all("tr")
LIST_OF_INTEREST_RATES = []

for i in rows[1:]:  # skipping heading
    data = i.find_all("td")
    row = [tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

final_rate = LIST_OF_INTEREST_RATES[1:]
final_rate = [row[:3] + row[5:] for row in final_rate]

for i in final_rate:
    super_senior_rate = float(i[1][:4]) + 0.75
    super_senior_rate = str(super_senior_rate) + '%'
    i.append(super_senior_rate)

final_rate = [[item.replace('\xa0', ' ') for item in sublist] for sublist in final_rate]

# Clean up the rates by removing 'Highest'
for i in final_rate:
    for j in range(1, 3):  # Columns 1 and 2 for gen_rate and sr_rate
        i[j] = i[j].replace('Highest', '').strip()

final_rates = []
for i in final_rate:
    x = ['RBL Bank']
    x.extend(i)
    x.insert(3, '')
    x.insert(5, '')
    x.insert(7, '') 
    x.append(30000000)
    final_rates.append(x)

print(final_rates)


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name,mode='a',header='False',index=False)




