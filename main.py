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
df = pandas.read_csv('contacts.csv')
yag = yagmail.SMTP(user=sender, password=my_password)

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

for index, row in df.iterrows():
    name = row['name']
    amount = str(row['amount'])     #this has to be a string in order for it to be written to our check.txt file
    receiver = row['email']
    generate_file(name, amount)
    
    email_body = [f"""
    Hi {name}! You must pay your bill, which is:
    {amount}.\nThank you.
    """, 'check.txt']                    #notice here we add check.txt to the list
    
    yag.send(to=receiver, subject=subject, contents=email_body)

print("Email sent successfully.\n")