#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id = reader.read_id()
        print(id)
finally:
        GPIO.cleanup()
