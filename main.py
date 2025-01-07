"""
using python to view data from a SQLite database. 

Can go to inloop.github.io/sqlite-viewer/ to view data contents if needed, but this is what we are trying to achieve in python
"""

import sqlite3

con = sqlite3.connect("./database.db")                  #sqlite needs to connect to our database to be able to work with it. we provide the path to our database to connect it.                           
cur = con.cursor()                                      #in order to execute SQL statements and fetch results from queries, we need a database cursor.

cur.execute("SELECT * FROM 'ips' ORDER BY asn")         #using .execute will execute whatever SQL query you give it inside of the string. in this case, we select all data from the ip's database table, and order it from least asn number to the greatest.
print(cur.fetchall())

#this is all there is to it. at this point, learning SQL is the only thing that remains.


#get all rows but only the address and asn columns, also ordering by asn number
# cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")         
# print(cur.fetchall())

#get all rows where asn number is less than 300
# cur.execute("SELECT * FROM 'ips', WHERE asn < 300")
# print(cur.fetchall())

#get all rows where asn number is less than 300 where the domain also ends in 'sa'
# cur.execute("SELECT * FROM 'ips', WHERE asn < 300 AND domain LIKE '%sa'")
# print(cur.fetchall())

'''
The LIKE operator is used in a WHERE clause to search for a 
specified pattern in a column. 

SYNTAX:

SELECT column1, column2, ... , columnN FROM table_name WHERE columnN LIKE pattern;

- https://www.w3schools.com/sql/sql_like.asp
'''




"""
what happens when set 2 different variables to store results after executing fetchall? 
you would think that both results1 and results2 would contain the same data, but if you
print results1 and results2 out, you will notice that results1 contains the information
that we specified, but results2 is an empty list. 

basically, once you run the SQL query once, then the list is exhausted, meaning when you
try to use it again in another query, it is empty.
"""
# cur.execute("SELECT * FROM 'ips', WHERE asn < 300 AND domain LIKE '%sa'")
# results1 = cur.fetchall()
# results2 = cur.fetchall()

#we can of course iterate through the contents in the results1 variable
#for row in results1:
#    print(row)




#to insert new rows into a SQL database:
# new_rows = [
#     ('100.100.100.100', 'a.b.c', 100),
#     ('200.200.200.200', 'd.e.f', 200)
# ]
# cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
# con.commit()
# cur.execute("SELECT * FROM 'ips'")
# print(cur.fetchall())