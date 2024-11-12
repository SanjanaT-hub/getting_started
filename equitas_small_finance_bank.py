import requests #fetches data from webpage
from bs4 import BeautifulSoup #extracts data we need
import pandas as pd #to store data as csv or excel format
import csv

url="https://www.equitasbank.com/personal-banking/save/fixed-deposits/fixed-deposit/"

r=requests.get(url)
print(r)
