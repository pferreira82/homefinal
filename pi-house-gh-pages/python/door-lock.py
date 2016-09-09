# Using a Solenoid with RPi.GPIO

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub

GPIO.setmode(GPIO.BCM)

PIN_DOOR = 18
PIN_LIVING = 4
PIN_FAN = 25

GPIO.setup(PIN_DOOR, GPIO.OUT)
GPIO.setup(PIN_LIVING, GPIO.OUT)
GPIO.setup(PIN_FAN, GPIO.OUT)

GPIO.output(PIN_DOOR, False)
GPIO.output(PIN_LIVING, False)
GPIO.output(PIN_FAN, False)


# PubNub

pubnub = Pubnub(publish_key='', subscribe_key='')

channel = 'pi-house'

def _callback(m, channel):
    print(m)

    if m['item'] == 'door':
        open_close = m['open']
        GPIO.output(PIN_DOOR, open_close)
    elif m['item'] == 'lightliving':
        on_off = m['on']
        GPIO.output(PIN_LIVING, on_off)
    elif m['item'] == 'fan':
        on_off = m['on']
        GPIO.output(PIN_FAN, on_off)


def _error(m):
  print(m)

pubnub.subscribe(channels=channel, callback=_callback, error=_error)

try:
    while 1:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)
