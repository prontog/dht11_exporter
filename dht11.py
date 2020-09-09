#!/usr/bin/python3

import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('temperature={device="dht11"}\nhumidity={1:0.1f}'.format(temperature, humidity))
else:
    print('')
