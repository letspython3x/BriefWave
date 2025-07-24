"""Email service for sending emails with IT circulars summaries."""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    """Responsible for composing and sending emails."""

    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject: str, text_content: str, html_content: str, receiver_email: str) -> bool:
        """Sends an email with both text and HTML content using SMTP."""
        if not all([subject, text_content, html_content, receiver_email]):
            raise ValueError("All parameters are required for sending an email.")

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = receiver_email

        # Attach plain text and HTML versions
        part_text = MIMEText(text_content, "plain")
        part_html = MIMEText(html_content, "html")

        message.attach(part_text)
        message.attach(part_html)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Secure the connection
                server.starttls(context=context)
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, receiver_email, message.as_string())
            print(f"Email sent successfully to {receiver_email}!")
            return True
        except Exception as e:
            msg = f"Error sending email: {e}. Please check your SENDER_EMAIL, SENDER_PASSWORD, and SMTP settings. For Gmail, ensure you are using an App Password if 2FA is enabled."
            print(msg)
            raise Exception(msg)
