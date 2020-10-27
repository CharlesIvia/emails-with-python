import os
import smtplib

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# connect to smtp mail server

# python -m smtpd -c DebuggingServer -n localhost:1025

with smtplib.SMTP("localhost", 1025) as smtp:
    subject = "Test Drive"
    body = "Hello, The car is ready for a test drive whenever you are."

    msg = f"Subject: {subject} \n\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "charlestitanmarket@gmail.com", msg)
