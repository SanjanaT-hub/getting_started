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


url = "https://sbi.co.in/web/interest-rates/deposit-rates/retail-domestic-term-deposits"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="table table-bordered")

rows = table.find_all("tr")
LIST_OF_INTEREST_RATES = []

for i in rows[2:]:  # skipping heading
    data = i.find_all("td")
    row = [tr.text for tr in data]
    LIST_OF_INTEREST_RATES.append(row)

# Clean and format interest rates
LIST_OF_INTEREST_RATES = [[sublist[i].replace('*', '').strip() + '%' if i in [2, 4] else sublist[i] for i in [0, 2, 4]] for sublist in LIST_OF_INTEREST_RATES]
final_rates = []

for i in LIST_OF_INTEREST_RATES:
    x = ['State Bank of India']
    x.extend(i)  # Add tenure and rates
    x.insert(3, '')  # Placeholder for annualised_gen_rates
    x.insert(5, '')  # Placeholder for annualised_sr_rates
    x.insert(6, '')  # Placeholder for super_sr_rates
    x.insert(7, '')  # Placeholder for annualised_super_sr_rates
    x.append(30000000)  # Threshold amount
    final_rates.append(x)

# Create DataFrame with the new columns
int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)

