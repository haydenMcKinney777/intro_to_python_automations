sender = my_email
receiver = 'haymckin@ttu.edu'
subject = 'Test subject v1'
email_body = """
This is the content body of the email.
This is also where information goes
Python
"""

msg = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{email_body}"     #smtp library interprets these email headers

try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)     #port 587 is used by smtp for encrypted mail transmissions
    server.set_debuglevel(1)                                #level 1 results in debug messages for connection
    server.starttls()                                       #all smtp commands that follow this line will be encrypted.
    server.login(my_email, my_password)
    server.sendmail(sender, receiver, msg)
    print("Email sent successfully!")

except Exception as e:
    print(f"ERROR: {e}")
    
finally:
    server.quit()