"""
converting SQL database to excel/csv file
"""

import sqlite3
import pandas

con = sqlite3.connect("./database.db")      
cur = con.cursor()

#we don't execute the query through cur as we did previously, but through pandas instead
df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)         #when using pandas to work with SQL, we need to specify both the query and the connection. 
print(df)

df.to_csv('database.csv', index=None)                                                               #converting our dataframe into a csv file is as simple as calling .to_csv and providing the file path that we want the csv file to be stored. index=None simply removes the indexing the pandas automatically places on each row.
df.to_excel('database.xlsx', index=None)                                                            #the only thing we need for this line to work is making sure we have 'openpyxl' installed i.e. pip install openpyxl
