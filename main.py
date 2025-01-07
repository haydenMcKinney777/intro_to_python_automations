"""
converting a SQL database into a PDF file. for further help with fpdf, visit section 7
"""

import sqlite3
from fpdf import FPDF

con = sqlite3.connect("./database.db")
cur = con.cursor()

#we want to iterate over each row in our database and create a cell for each element within that row
cur.execute('PRAGMA table_info(ips)')                                               #this command gives us info about the ips table columns
columns = cur.fetchall()                                                            #recall fetchall fetches all rows and returns a list of tuples, but because of the line above, we get the columns instead

pdf = FPDF(orientation='P', unit='pt', format='A4')                                 #create pdf instance with portrait orientation
pdf.add_page()

for column in columns:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=30, txt=column[1], border=1)

pdf.ln()                                                                            #line break 

cur.execute('SELECT * FROM "ips"')                                                  #select all rows from database
rows = cur.fetchall()

for row in rows:
    for element in row:
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=30, txt=str(element), border=1)                           #we need to ensure that every element within the rows are strings (since for example, asn is included in the row and it is an integer)
    pdf.ln()

pdf.output('output.pdf')