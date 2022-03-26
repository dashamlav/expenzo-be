from django.conf import settings
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_otp_email(toEmail, name, otp):
    PORT = 465
    context = ssl.create_default_context()
    expenzo_email = settings.EXPENZO_EMAIL
    password = settings.SMTP_PASS

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(expenzo_email, password)
        message = MIMEMultipart("alternative")
        message["Subject"] = "OTP for verification"
        message["From"] = expenzo_email
        message["To"] = toEmail

        html_text = f"""\
            <html>
                <body>
                    <p> Hello {name}, </p>
                    <p> The OTP to register your Expenzo account is <strong>{otp}</strong>. Please do not share this one-time password with anyone. </p>
                    <p> This is an automated email. Please do not reply to this email. </p>
                </body>
            </html>
        """
        html = MIMEText(html_text, "html")
        message.attach(html)

        server.sendmail(expenzo_email, toEmail, message.as_string())