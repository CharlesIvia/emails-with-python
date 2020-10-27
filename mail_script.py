import os
import smtplib
from email.message import EmailMessage

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# Contact list

contacts = ["charlestitanmarket@gmail.com", "iviacharles@gmail.com"]

# Create email

msg = EmailMessage()
msg["Subject"] = "Test Drive this weekend"
msg["From"] = EMAIL_ADDRESS
msg["To"] = contacts
msg.set_content("Hello, The car is ready for a test drive whenever you are.")

# connect to smtp mail server

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
