#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import json
import matplotlib.pyplot as plt
from pprint import pprint

print("The exchange rate at the beginning of each year for a chosen currency against PLN over the last 20 years(2005 - 2025) according to NBP data")
print()
dates = [
    "2005-01-03","2006-01-02","2007-01-02","2008-01-02","2009-01-02","2010-01-04",
    "2011-01-03","2012-01-02","2013-01-02","2014-01-02","2015-01-02", "2016-01-04", 
    "2017-01-02", "2018-01-02", "2019-01-02","2020-01-02", "2021-01-04", "2022-01-03", 
    "2023-01-02", "2024-01-02", "2025-01-02"
]

def exchangeRates(code, date):
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json"
    try:
        r = requests.get(url)
        rates = r.json()
        #pprint(rates)
        return rates
    except requests.exceptions.RequestException as e:
        return None

while True:
    print("1: Choose currency")
    print("2: Exit")
    choice = input("What would you like to do?: ")
    if choice == "1":
        code = input("Choose currency (e.g. USD, EUR, CHF): ")
        code = code.upper()
        
        exchange_rates_dict = {}
    
        for date in dates:
            rate = exchangeRates(code, date)
            if rate is not None:
                exchange_rate = rate["rates"][0]["mid"]
                exchange_rates_dict[date] = exchange_rate

        print()
        print(f"The exchange rate at the beginning of each year for {code} against PLN 2005-2025")
        for date, rate in exchange_rates_dict.items():
            print(f"{date}: {rate}")
            
        exchange_rates_dict = {key.split("-")[0]: value for key, value in exchange_rates_dict.items()}

        plt.figure()
        plt.plot(exchange_rates_dict.keys(), exchange_rates_dict.values(), color='green',marker='o')
        plt.xlabel("Year")
        plt.ylabel("Exchange rate")
        plt.grid(True)
        plt.title(f"The exchange rate at the beginning of each year for {code} against PLN 2005-2025")
        plt.xticks(rotation=45)
        plt.show()
    elif choice == "2":
        break
    else:
        print("Please choose number 1 or 2")

