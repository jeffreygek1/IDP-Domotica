import RPi.GPIO as GPIO
import time
import os
import MySQLdb


RED = 17
GREEN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

db = MySQLdb.connect(host='idp-projectserver.ddns.net', user='raspberry1',
                              passwd='raspberry', db='domoDB')


def noodknop():
    while True:
        if GPIO.input(21) == True:
            print("noodknop ingedrukt!")
            camera_aan()
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
    sql = "UPDATE Monitor SET  geeftnoodoproep = 1 WHERE rpiID = 1 and woningnr = 1"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    return
noodknop()