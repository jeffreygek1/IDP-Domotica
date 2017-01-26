import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def knop_LED():
    while True:
        if GPIO.input(24) == True:
            print("knop in gedrukt...")
            time.sleep(0.3)
            print("Lamp gaat aan...")
            LED()

def LED():
    os.system("sudo service motion stop")
    GPIO.output(17, True)
    time.sleep(5)
    GPIO.output(17, False)
    return


os.system("sudo service motion start")
os.system("sudo motion")
knop_LED()


