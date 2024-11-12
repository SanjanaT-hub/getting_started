import requests
from bs4 import BeautifulSoup
import pandas as pd #to store data as csv or excel format
import csv

# Fetch the webpage
url = "https://www.cityunionbank.com/deposit-interest-rate"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Find the first table
table = soup.find_all("table")[0]  # Assuming the first table is the one you need
rows = table.find_all("tr")

LIST_OF_INTEREST_RATES = []

# Extract data from the first table
for row in rows[2:13]:
    cells = row.find_all("td")
    row_data = [tr.text.strip() for tr in cells]  # Use strip() to clean whitespace
    LIST_OF_INTEREST_RATES.append(row_data)

# Find the second table
table = soup.find_all("table")[1]
rows = table.find_all("tr")

# Extract data from the second table
for index, row in enumerate(rows[2:]):  # Use enumerate to keep track of the index
    cells = row.find_all("td")
    row_data = [tr.text.strip() for tr in cells]
    
    # Append the relevant data only if index is valid
    if index < len(LIST_OF_INTEREST_RATES):
        LIST_OF_INTEREST_RATES[index].append(row_data[1])  # Only add the second column value

# Print the extracted data
print("LIST OF INTEREST RATES:", LIST_OF_INTEREST_RATES)




final_rates=[]
for i in LIST_OF_INTEREST_RATES:
    x=['Punjab National Bank']
    x.extend(i)
    x.append(30000000)
    final_rates.append(x)
print(final_rates)


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','sr_rate','super_sr_rate','threshold_amt'])


pd.set_option('display.max_columns',None)
print(int_rate_df)

int_rate_df.to_csv('Interest_Rates(city_union_bank).csv',mode='a',header='False',index=False)
