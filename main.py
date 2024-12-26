"""
sending emails periodically

TO-DO: does 24 hour sleep work?
"""

import yagmail
import os
from datetime import datetime as dt
import time

#accessing environment variables that i set up on my local machine to keep email and password safe.
my_email = os.getenv('gmail_email')         
my_password = os.getenv('app_password_gmail')

sender = my_email
receiver = os.getenv('email')           #my personal email
subject = 'Test subject v1'
email_body = """
This is the content body of the email.
You can put whatever information you want here!

this was an automated email sent by me.
thanks for reading!
"""

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 6:
        yag = yagmail.SMTP(user=sender, password=my_password)
        yag.send(to=receiver, subject=subject, contents=email_body)
        print("Email sent successfully")
        #yagmail cleans up itself automatically
        time.sleep(60)       #sleep for 1 minute