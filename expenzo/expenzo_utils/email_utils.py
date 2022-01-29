from django.conf import settings
import smtplib, ssl


def send_otp_email(toEmail, name, otp):
    PORT = 465
    context = ssl.create_default_context()
    password = settings.SMTP_PASS

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login("expenzoapp@gmail.com", password)
        message = f'Hello {name}, the OTP to register your Expenzo account is {otp}'
        server.sendmail("expenzoapp@gmail.com", toEmail, message)