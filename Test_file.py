import RPi.GPIO as GPIO
import time
import os
import MySQLdb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

RED = 17
GREEN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

db = MySQLdb.connect(host='idp-projectserver.ddns.net', user='raspberry1',
                              passwd='raspberry', db='domoDB')

def knop_LED():
    while True:
        if GPIO.input(24) == True:
            print("knop in gedrukt...")
            time.sleep(0.3)
            print("Camera gaat uit...")
            email()
            LED()

        if GPIO.input(23) == True:
            print("knop in gedrukt...")
            time.sleep(0.3)
            print("Camera gaat aan...")
            camera_aan()
            email()
        time.sleep(0.1)


def LED():
    GPIO.output(GREEN, False)
    GPIO.output(RED, True)
    os.system("sudo service motion stop")
    for i in range(0, 25):
        GPIO.output(RED, False)
        time.sleep(0.1)
        GPIO.output(RED, True)
        time.sleep(0.1)
    GPIO .output(RED, True)

def camera_aan():
    GPIO.output(RED, False)
    GPIO.output(GREEN, True)
    os.system("sudo service motion start")
    os.system("sudo motion")
    return

def database_noodknop():
    cursor = db.cursor()
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    return

def email():
    fromaddr = "rpi1domotica@gmail.com"
    toaddr = "jeffrey.gek@hotmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE MAIL"

    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Qazwsx1!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

os.system("sudo service motion start")
os.system("sudo motion")
GPIO.output(GREEN, True)
knop_LED()
db.close()
