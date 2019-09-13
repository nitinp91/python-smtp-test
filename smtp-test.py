# Step 1 - Import required packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# Step 2 - Create message object instance
msg = MIMEMultipart()
 
# Step 3 - Create message body
message = "SMTP Test email using Python"
 
# Step 4 - Declare SMTP credentials
username = "<SMTP_USERNAME>"
password = "<SMTP_Paassord>"
smtphost = "<SMTP_HOST>:<SMTP_PORT>"

# Step 5 - Declare message elements
msg['From'] = "<FROM_EMAIL_ID>"
msg['To'] = "<TO_EMAIL_ID>"
msg['Subject'] = "SMTP TEST"
 
# Step 6 - Add the message body to the object instance
msg.attach(MIMEText(message, 'plain'))
 
# Step 7 - Create the server connection
server = smtplib.SMTP(smtphost)
 
# Step 8 - Switch the connection over to TLS encryption
server.starttls()
 
# Step 9 - Authenticate with the server
server.login(username, password)
 
# Step 10 - Send the message
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Step 11 - Disconnect
server.quit()
 
# Step 12 - 
print ("Successfully sent email message")
