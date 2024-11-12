
import pandas as pd #to store data as csv or excel format
import csv
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)


final_rates = [
    ["Unity Small Finance Bank", "7 - 14 Days", "4.50%", "", "4.50%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "15 - 45 Days", "4.75%", "", "4.75%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "46 - 60 Days", "5.75%", "", "6.25%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "61 - 90 Days", "6.00%", "", "6.50%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "91 - 164 Days", "6.25%", "", "6.75%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "165 Days - 6 Months", "6.25%", "", "6.75%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "> 6 Months - 201 Days", "8.50%", "", "9.00%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "202 - 364 Days", "7.25%", "", "7.75%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "1 Year", "7.85%", "", "8.35%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "1 Year 1 day", "7.85%", "", "8.35%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "> 1 Year 1 day - 500 days", "7.85%", "", "8.35%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "501 Days", "8.75%", "", "9.25%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "502 Days - 18 Months", "7.85%", "", "8.35%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "> 18 Months - 700 Days", "7.90%", "", "8.40%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "701 Days", "8.75%", "", "9.25%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "702 Days - 1000 Days", "7.90%", "", "8.40%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "1001 Days", "9.00%", "", "9.50%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "1002 Days - 3 Year", "8.15%", "", "8.65%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "> 3 Year - 5 Year", "8.15%", "", "8.65%", "", "", "", 30000000],
    ["Unity Small Finance Bank", "> 5 Year - 10 Year", "7.50%", "", "8.00%", "", "", "", 30000000]
]
    


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)


