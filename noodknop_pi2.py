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
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

db = MySQLdb.connect(host='idp-projectserver.ddns.net', user='raspberry1',
                              passwd='raspberry', db='domoDB')

pi = "raspberry pi 2"


def noodknop():
    while True:
        if GPIO.input(21) == True:
            print("noodknop ingedrukt!")
            camera_aan()
            email()
            database_noodknop()
        time.sleep(0.3)

def camera_aan():
    GPIO.output(RED, False)
    GPIO.output(GREEN, True)
    os.system("sudo service motion start")
    os.system("sudo motion")
    return

def database_noodknop():
    cursor = db.cursor()
    sql = "UPDATE Monitor SET  geeftnoodoproep = 1 WHERE rpiID = 2 and woningnr = 2"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    return

def database_startup():
    cursor = db.cursor()
    sql = "UPDATE Monitor SET  geeftnoodoproep = 0 WHERE rpiID = 2 and woningnr = 2"
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
    toaddr = "jan.dekker@student.hu.nl"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "%s" % pi

    body = "%s heeft de noodknop ingedrukt" % pi
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Qazwsx1!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
database_startup()
noodknop()