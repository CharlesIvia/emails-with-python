import os
import smtplib
from email.message import EmailMessage

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# Create email

msg = EmailMessage()
msg["Subject"] = "Test Drive this weekend"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "charlestitanmarket@gmail.com"
msg.set_content("Hello, The car is ready for a test drive whenever you are.")

# connect to smtp mail server

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, "Xanadu2020")
    smtp.send_message(msg)
