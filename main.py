"""
sending emails including attachments, such as .txt files

really, all you have to do is put the contents of the email into a list

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
    email_body = [f"""
    Hi {row['name']}! This email has been automated using python.
    
    Thanks for reading! 
    
    -Python
    """, 'text.txt']                    #notice here we add text.txt to the list
    yag.send(to=row['email'], subject=subject, contents=email_body)
print("Email sent successfully.\n")