import os
import smtplib
import imghdr
from email.message import EmailMessage

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# Create email

msg = EmailMessage()
msg["Subject"] = "Earnest Hemmingway"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "charlestitanmarket@gmail.com"
msg.set_content("Check out Earnest Hemmingway")

files = ["./imgs/earnest.jpg", "./imgs/new.jpg", "./imgs/t_cvd.jpg"]

for file in files:
    with open(file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="image", subtype=file_type, filename=file_name
    )

# connect to smtp mail server

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
