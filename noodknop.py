import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def noodknop():
    while True:
        if GPIO.input(21) == True:
            print("noodknop ingedrukt!")
        time.sleep(0.1)

noodknop()