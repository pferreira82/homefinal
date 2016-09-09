import os
import time
import sys
from pubnub import Pubnub
import Adafruit_DHT as dht
import threading

pubnub = Pubnub(publish_key='', subscribe_key='')
channel = 'pi-house-temp'

def callback(message):
    print(message)
    

while True:
    h,t = dht.read_retry(dht.DHT22, 22)
    te = ((t * 9) / 5) + 32
    temp= round(te, 0)
    hum = round(h, 0)

    message = {'temperature': temp, 'humidity': hum}
    time.sleep(20)
    print ('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
    time.sleep(20)
    pubnub.publish(channel=channel, message=message, callback=callback, error=callback)
    time.sleep(20)     

    
    


