import os
import smtplib

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# connect to smtp mail server

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # Encrypt traffic
    smtp.ehlo()  # Identify ourself after encryption

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = "Test Drive"
    body = "Hello, The car is ready for a test drive whenever you are."

    msg = f"Subject: {subject} \n\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "charlestitanmarket@gmail.com", msg)
