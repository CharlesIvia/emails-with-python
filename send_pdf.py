import os
import smtplib
import imghdr
from email.message import EmailMessage

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# Create email

msg = EmailMessage()
msg["Subject"] = "RESUME"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "charlestitanmarket@gmail.com"
msg.set_content("Check out my resume")

files = ["./imgs/resume.pdf"]

for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="application", subtype="octet-stream", filename=file_name
    )

# connect to smtp mail server

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
