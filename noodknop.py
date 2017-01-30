import RPi.GPIO as GPIO
import time
import os


RED = 17
GREEN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def noodknop():
    while True:
        if GPIO.input(21) == True:
            print("noodknop ingedrukt!")
            camera_aan()
        time.sleep(0.3)

def camera_aan():
    GPIO.output(RED, False)
    GPIO.output(GREEN, True)
    os.system("sudo service motion start")
    os.system("sudo motion")
    return

noodknop()