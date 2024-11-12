import requests  # fetches data from webpage
from bs4 import BeautifulSoup  # extracts data we need
import pandas as pd  # to store data as csv or excel format
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)


url = "https://www.pnbindia.in/Interest-Rates-Deposit.html"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
table = soup.find_all("table")

if len(table) > 1:
    table = table[16]
rows = table.find_all("tr")

LIST_OF_INTEREST_RATES = []

for i in rows[2:]:  # skipping heading
    data = i.find_all("td")
    row = [tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

cleaned_data = [[cell.replace('\n', '').replace('\r', '').strip() for cell in row] for row in LIST_OF_INTEREST_RATES]

# Print the cleaned rates
final_rates = []
for i in cleaned_data:
    x = ['Punjab National Bank']
    x.extend(i[1:])  # Add tenure and rates
    x.insert(3, '')  # Placeholder for annualised_gen_rate
    x.insert(5, '')  # Placeholder for annualised_sr_rate
    x.insert(7, '')  # Placeholder for annualised_super_sr_rate
    x.append(30000000)
    final_rates.append(x)

int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)


