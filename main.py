"""
Exercise 6: send email with attachment to a list of contacts in a CSV file
"""

import pandas as pd
import yagmail
import os

df = pd.read_csv("./contacts.csv")

sender = os.getenv("gmail_email")
password = os.getenv("app_password_gmail")
yag = yagmail.SMTP(sender, password)
subject = "Automated email with attachment"

for index, row in df.iterrows():
    contents = [f"""Hello {row["name"]}! This is an automated email sent to you ({row['email']})
              using python.
              
              This email has an attachment on it as well!
              Thanks for reading.
              """, "attachment.txt"]

    yag.send(to=row['email'], subject=subject, contents=contents)
print("Emails sent successfully")