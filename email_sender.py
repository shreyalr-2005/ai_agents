import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, password

subject = "Test Email from Python"
body = "Hello! This email was sent using Python."

# Create email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()          # Secure connection
    server.login(sender_email, password)
    server.send_message(msg)

print("Email sent successfully!")
