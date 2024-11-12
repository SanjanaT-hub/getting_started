import pandas as pd #to store data as csv or excel format
import csv
from datetime import date

today = date.today()

# dd/mm/yy
date1 = today.strftime('%d%m%Y')
print(date1)
file_name = 'Interest_rate_' + date1 + '.csv'
print(file_name)




# Rows from the table
final_rates=[['Utkarsh Small Finance Bank', '7 Days to 45 Days', '4.00%','', '4.60%','','' ,'',30000000],
 ['Utkarsh Small Finance Bank', '46 Days to 90 Days', '4.75%','', '5.35%','','','', 30000000],
 ['Utkarsh Small Finance Bank', '91 Days to 180 Days', '5.50%','', '6.10%','','','', 30000000],
 ['Utkarsh Small Finance Bank', '181 Days to 364 Days', '6.50%', '','7.10%', '','','',30000000],
 ['Utkarsh Small Finance Bank', '365 Days to 699 Days', '8.00%', '','8.60%','','','', 30000000],
 ['Utkarsh Small Finance Bank', '700 Days to less than 2 Years', '8.25%','', '8.85%','','','', 30000000],
 ['Utkarsh Small Finance Bank', '2 Years upto 3 Years', '8.50%', '','9.10%','','','', 30000000],
 ['Utkarsh Small Finance Bank', 'Above 3 Years to less than 4 Years', '8.25%','', '8.85%','','','', 30000000],
 ['Utkarsh Small Finance Bank', '4 Years upto 5 Years', '7.50%', '','8.10%','','','', 30000000],
 ['Utkarsh Small Finance Bank', 'Above 5 Years upto 10 Years', '7.00%','', '7.60%','','','', 30000000]]


int_rate_df=pd.DataFrame(final_rates,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)



