import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, password

# Create email
def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the given receiver with the specified subject and content."""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

# Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()          # Secure connection
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")
