import imaplib
import os
import email

# Get email and password from env

EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

M = imaplib.IMAP4_SSL("imap.gmail.com")

M.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

print(M.list())

M.select("inbox")
typ, data = M.search(None, "SUBJECT 'Color'")
print(typ)
print(data)
email_id = data[0]

result, email_data = M.fetch(email_id, "(RFC822)")
print(email_data)

# email_data

raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

email_message = email.message_from_string(raw_email_string)
print(email_message)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
