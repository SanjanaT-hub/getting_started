from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
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


# Set up the Chrome driver
chrome_driver_path = 'c:\\Users\\dellp\\Downloads\\WEBSCRAPINGFILES\\chromedriver-win64\\chromedriver.exe'

chrome_options=Options()
chrome_options.add_argument("--headless") # enables headless mode

service=Service(chrome_driver_path)

driver = webdriver.Chrome(service=service,options=chrome_options)

# Navigate to the URL
url = "https://www.iob.in/Domestic_Rates"
driver.get(url)

# Wait for the JavaScript to execute (you can adjust the sleep time if needed)
time.sleep(5)  # Wait for 5 seconds

# Get the rendered HTML
html = driver.page_source

# Display the HTML
#print(html)

# Close the driver
driver.quit()
#################################################
soup=BeautifulSoup(html,"xml")
#print(soup.prettify())


table=soup.find("table")
#print(table)
#table=soup.find_all("table",{'class': 'rates-table-main'})
#if len(table)>1:
#   table=table[0]

rows=table.find_all("tr")
LIST_OF_INTEREST_RATES=[]

for i in rows[1:]:  #skipping heading

    data=i.find_all("td")
    #print(data)
    row=['Indian Overseas Bank']
    row.extend([tr.text for tr in data])
    row.append(30000000)
    LIST_OF_INTEREST_RATES.append(row)



'''for i in LIST_OF_INTEREST_RATES:
    print(i)'''
    

int_rate_df=pd.DataFrame(LIST_OF_INTEREST_RATES,columns=['bank_name','tenure','gen_rate','annualised_gen_rate','sr_rate','annualised_sr_rate','super_sr_rate','annualised_super_sr_rate','threshold_amt'])

pd.set_option('display.max_columns', None)
print(int_rate_df)

int_rate_df.to_csv(file_name, mode='a', header=False, index=False)

