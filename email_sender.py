import smtplib, ssl
import datetime

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "felipe.valencia2003@gmail.com"
receiver_email = "your@gmail.com"  # Enter receiver address
password = "password"
message1 = """\
Subject: Intruder Detected.

Your Infrared Sensor has registered movement at """ + str(datetime.datetime.now())

message2 = """\
Subject: Detector has been tampered with.

Your Tilt Switch been moved and triggered at """ + str(datetime.datetime.now())


def detected(infra_or_tilt):
    message = ""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        if infra_or_tilt == 1:
            message = message1
        else:
            message = message2
        server.sendmail(sender_email, receiver_email, message1)
