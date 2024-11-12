import requests  # fetches data from webpage
from bs4 import BeautifulSoup  # extracts data we need
import pandas as pd  # to store data as csv or excel format
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)

url = "https://bandhanbank.com/rates-charges"
r = requests.get(url)
print(r)

def rate_data(table):
    rows = table.find_all("tr")

    for i in rows[1:]:  # skipping heading
        data = i.find_all("td")
        row = [tr.text for tr in data]
        LIST_OF_INTEREST_RATES.append(row)

soup = BeautifulSoup(r.text, "lxml")
table = soup.find_all("table", class_="table")
if len(table) > 1:
    table1 = table[4]
    table2 = table[5]

headings = ["Maturity Bucket", "Interest Rates for Non-Senior Citizens", "Interest Rates for Senior Citizens"]
LIST_OF_INTEREST_RATES = []
rate_data(table1)
rate_data(table2)

# Remove empty lists
LIST_OF_INTEREST_RATES = [i for i in LIST_OF_INTEREST_RATES if i]

final_rates = []
for i in LIST_OF_INTEREST_RATES:
    
    x = ['Bandhan Bank']
    x.extend(i)
    x.insert(3, '')  # Placeholder for annualised_gen_rate
    x.insert(5, '')  # Placeholder for annualised_sr_rate
    x.insert(6, '')
    x.insert(7,'')# Placeholder for annualised_super_sr_rate
    x.append(30000000)  # Threshold amount
    final_rates.append(x)
for i in final_rates:
    print(i)

#print(final_rates)

# Create DataFrame with the new columns
int_rate_df = pd.DataFrame(final_rates, columns=[
    'bank_name', 'tenure', 'gen_rate', 'annualised_gen_rate',
    'sr_rate', 'annualised_sr_rate', 'super_sr_rate', 
    'annualised_super_sr_rate', 'threshold_amt'
])

pd.set_option('display.max_columns', None)
print(int_rate_df)

file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)
int_rate_df.to_csv(file_name, mode='a', header=False, index=False)
 


