import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get email credentials from the environment
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Email details
sender_email = EMAIL_USER
receiver_email = "vaibhavkanodia2565@gmail.com"
subject = "Test Email from Python"
body = "This is a test email sent from Python."

# Create the email content
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

try:
    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Upgrade the connection to secure
    server.login(EMAIL_USER, EMAIL_PASS)  # Log in to the email account

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the server connection
    server.quit()
