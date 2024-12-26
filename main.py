"""
sending emails to contacts found within a CSV file

"""

import yagmail
import os
import pandas

#accessing environment variables that i set up on my local machine to keep email and password safe.
my_email = os.getenv('gmail_email')         
my_password = os.getenv('app_password_gmail')

sender = my_email
subject = 'Automated email test'
yag = yagmail.SMTP(user=sender, password=my_password)

df = pandas.read_csv('contacts.csv')    #we use pandas to help us analyze our data in the csv file. 'df' = "dataframe"
for index, row in df.iterrows():
    email_body = f"""
    Hi {row['name']}! This email has been automated using python.
    
    Thanks for reading! 
    
    -Python
    """
    yag.send(to=row['email'], subject=subject, contents=email_body)
print("Email sent successfully.\n")