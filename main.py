"""
Using yagmail gmail/smtp client to send single emails using python

here i am sending an email with my gmail account to my personal email since i just wanted to try this on myself
however to send to anyone else simply replace 'receiver' variable with whoever you want to send the email to

note yagmail only works with gmail accounts - can't send mail with any other type of account

docs: https://yagmail.readthedocs.io/en/latest/
"""

import yagmail
import os

#accessing environment variables that i set up on my local machine to keep email and password safe.
my_email = os.getenv('gmail_email')         
my_password = os.getenv('app_password_gmail')

sender = my_email
receiver = os.getenv('email')           #my personal email
subject = 'Test subject v1'
email_body = """
This is the content body of the email.
This is also where information goes
Python
"""

yag = yagmail.SMTP(user=sender, password=my_password)
yag.send(to=receiver, subject=subject, contents=email_body)
print("Email sent successfully")
#yagmail cleans up itself automatically