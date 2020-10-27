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
msg.set_content("Hello, The is plain text email")

msg.add_alternative(
    """\
    <!DOCTYPE html>
    <html>
    <body>
        <h1 style="color: coral;">This is an HTML email! </h1>
    </body>
                    
    </html>
                    """,
    subtype="html",
)

# connect to smtp mail server

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, "Xanadu2020")
    smtp.send_message(msg)
