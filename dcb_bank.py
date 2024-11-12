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



# Fetch the webpage
url = "https://www.dcbbank.com/zippi-online-fixed-deposit/deposit-rates"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Find the first table
table = soup.find_all("table")[2]

rows = table.find_all("tr")

LIST_OF_INTEREST_RATES = []

for row in rows[3:]:
    cells = row.find_all("td")
    row = [tr.text for tr in cells]
    LIST_OF_INTEREST_RATES.append(row)

print(LIST_OF_INTEREST_RATES)

final_rates = []
for i in LIST_OF_INTEREST_RATES:
    x = ['DCB Bank']
    x.extend(i)
    x.append('')  # Placeholder for super_sr_rate
    x.append('')  # Placeholder for annualised_super_sr_rate
    x.append(30000000)  # Threshold amount
    final_rates.append(x)

# Create DataFrame with the new columns
int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)

