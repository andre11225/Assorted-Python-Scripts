# This program simply sends a simple email with text, that's all. 
# Never know when you might need to quickly send out and email

import smtplib

# Source email address
fromaddr = ''

# Destination email address
toaddrs = ''

# Message being sent to the receivor
msg = ''

# Login info of the sender's email account
username = ''
password = ''


# The server address being used to send the email, must be a valid server

# Google's server
server = smtplib.SMTP('smtp.gmail.com:587')


# Process that sends email
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
