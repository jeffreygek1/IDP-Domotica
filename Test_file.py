import RPi.GPIO as GPIO
import time
import os

RED = 17
GREEN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def knop_LED():
    while True:
        if GPIO.input(24) == True:
            print("knop in gedrukt...")
            time.sleep(0.3)
            print("Lamp gaat aan...")
            LED()

        if GPIO.input(23) == True:
            print("knop in gedrukt...")
            time.sleep(0.3)
            print("Lamp gaat aan...")
            camera_aan()
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

os.system("sudo service motion start")
os.system("sudo motion")
GPIO.output(GREEN, True)
knop_LED()
