import pandas as pd #to store data as csv or excel format
import csv
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)


final_rates = interest_rates = [
    ['Axis Bank', '7 – 14 days', '3.00%', '', '3.50%', '', '', '', 30000000],
    ['Axis Bank', '15 – 29 days', '3.00%', '', '3.50%', '', '', '', 30000000],
    ['Axis Bank', '30 – 45 days', '3.50%', '', '4.00%', '', '', '', 30000000],
    ['Axis Bank', '46 – 60 days', '4.25%', '', '4.75%', '', '', '', 30000000],
    ['Axis Bank', '61 days < 3 months', '4.50%', '', '5.00%', '', '', '', 30000000],
    ['Axis Bank', '3 months – 3 months 24 days', '4.75%', '', '5.25%', '', '', '', 30000000],
    ['Axis Bank', '3 months 25 days < 4 months', '4.75%', '', '5.25%', '', '', '', 30000000],
    ['Axis Bank', '4 months < 5 months', '4.75%', '', '5.25%', '', '', '', 30000000],
    ['Axis Bank', '5 months < 6 months', '4.75%', '', '5.25%', '', '', '', 30000000],
    ['Axis Bank', '6 months < 7 months', '5.75%', '', '6.25%', '', '', '', 30000000],
    ['Axis Bank', '7 months < 8 months', '5.75%', '', '6.25%', '', '', '', 30000000],
    ['Axis Bank', '8 months < 9 months', '5.75%', '', '6.25%', '', '', '', 30000000],
    ['Axis Bank', '9 months < 10 months', '6.00%', '', '6.50%', '', '', '', 30000000],
    ['Axis Bank', '10 months < 11 months', '6.00%', '', '6.50%', '', '', '', 30000000],
    ['Axis Bank', '11 months – 11 months 24 days', '6.00%', '', '6.50%', '', '', '', 30000000],
    ['Axis Bank', '11 months 25 days < 1 year', '6.00%', '', '6.50%', '', '', '', 30000000],
    ['Axis Bank', '1 year – 1 year 4 days', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '1 year 5 days – 1 year 10 days', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '1 year 11 days – 1 year 24 days', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '1 year 25 days < 13 months', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '13 months < 14 months', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '14 months < 15 months', '6.70%', '', '7.20%', '', '', '', 30000000],
    ['Axis Bank', '15 months < 16 months', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '16 months < 17 months', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '17 months < 18 months', '7.20%', '', '7.70%', '', '', '', 30000000],
    ['Axis Bank', '18 Months < 2 years', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '2 years < 30 months', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '30 months < 3 years', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '3 years < 5 years', '7.10%', '', '7.60%', '', '', '', 30000000],
    ['Axis Bank', '5 years to 10 years', '7.00%', '', '7.75%', '', '', '', 30000000]
]


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)










