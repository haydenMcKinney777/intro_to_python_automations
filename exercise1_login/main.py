"""
STOCK DATA: Ask user for ticket symbol, start & end date, use that data to search for that specific stock
            during the time period that the user gave and process the data into a new csv file.

TO DO: figure out how to get a reliable URL. so far, I have not been able to find any way of copying the link to the 
       "download" button on the stock's historical data

"""

import requests                                                                             #needed for GET request for our URL
from datetime import datetime
import time

ticker_symbol = input("Enter the ticker symbol for the stock data you would like to view: ")
from_date = input("Enter the date to start from in yyyy-mm-dd: ")
to_date = input("Enter the date to end at in yyyy-mm-dd: ")

try:
    from_datetime = datetime.strptime(from_date, '%Y-%m-%d')                                #validate date format
    to_datetime = datetime.strptime(to_date, '%Y-%m-%d')
except ValueError:
    print("Invalid date format. Please enter dates in yyyy-mm-dd format.")
    exit()

from_date_formatted = from_datetime.strftime('%Y-%m-%d')
to_date_formatted = to_datetime.strftime('%Y-%m-%d')

# from_epoch = int(from_datetime.timestamp())
# to_epoch = int(to_datetime.timestamp())

url = f"https://api.nasdaq.com/api/quote/{ticker_symbol}/historical?assetclass=stocks&fromdate={from_date_formatted}&limit=9999&todate={to_date_formatted}&random=24"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} #these headers are used to basically disguise ourselves from the webpage we're accessing, making us look like a regular browser

content = requests.get(url, headers=headers).content                                        #this is the content that the GET request will return

with open("data.csv", "wb") as file:                                                        #note that 'wb' is a more general write option. it is able to deal with both byte-data and non byte-data. if we were to only use "w" we could only work with text data, which would also mean we would have to use .text instead of .content on the line above
    file.write(content)
