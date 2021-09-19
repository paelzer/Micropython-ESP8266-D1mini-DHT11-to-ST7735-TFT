import network
import os
import sys
from umqtt.robust import MQTTClient
from machine import Pin, SPI
from time import sleep
import st7735
import bitmapfont
import gc
from dht import DHT11

gc.enable()

# ****************************** ADAFRUIT IO connection related ********************************
# *
# **********************************************************************************************

# Sign of life LED - setup GPIO2 as an output pin connected to the onboard LED
#
ledPin = Pin(2, Pin.OUT, value=1)

# A randomly created MQTT clientID
# (see https://io.adafruit.com/api/docs/mqtt.html#adafruit-io-mqtt-api for more details about the API)
#
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

# Your IO.ADAFRUIT.COM account data
#
ADAFRUIT_IO_URL = b'io.adafruit.com' 
ADAFRUIT_USERNAME = b'Your Adafruit username'
ADAFRUIT_IO_KEY = b'Your Adafruit IO KEY'
ADAFRUIT_IO_FEEDNAME = b'Your Adafruit feed name'

# Establish connection to Adafruit IO MQTT via unsecure TCP port 1883
# 
# For secured SSL connection set set parameter ssl from "ssl=False" to "ssl=True"
# Note: SSL connection uses about 9k bytes of the heap means 25% of the ESP8266 heap
#
client = MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)
try:            
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

# send temperature measured by the DHT11 sensor to Adafruit IO via MQTT
#
# format of feed name:  
# "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')
PUBLISH_PERIOD_IN_SEC = 10


# **************************** DHT11 sensor & ST7735 TFT related *******************************
# *
# **********************************************************************************************
#
# This initiates the SPI bus
#
display = st7735.ST7735R(SPI(1, baudrate=40000000), dc=Pin(16), cs=Pin(15), rst=Pin(0))

bf = bitmapfont.BitmapFont(128,160, display.pixel)
bf.init()

dht11sensor = DHT11(Pin(12))

# sensor values initially 0
temp = 0
hum = 0
mf = 0

# store old sensor values
old_temp = temp
old_hum = hum
old_mf = mf

# clear the display
display.fill(0)

# heading
bf.text("DHT11 Sensor values:", 0, 5, 0xffff)

# put sensor values names on the display
bf.text("Temperature", 7, 35, 0xffff)
bf.text("Humidity", 7, 67, 0xffff)
bf.text("Free memory:", 7, 130, 0xffff)

# draw a table
"""
Example for better understanding how display.vline and display.hline work:
    The following 2 lines draw a horizontal and a vertical line:
    The horizontal line goes from pixel row 5/column 10 (start counting from zero) and is 10 pixel long
    The vertical line goes from pixel row 5/column 10 (start counting from zero) and is 7 pixel long
    Color is white in both cases

display.hline(4, 10, 10, color=0xffff)
display.vline(4, 10, 7, color=0xffff)

   012345678910...........  
  |-----------------------
 0|.......................
 1|.......................
 2|.......................
 3|.......................
 4|......... **********...
 5|..........*............
 6|..........*............
 7|..........*............
 8|..........*............
 9|..........*............
10|..........*............
11|.......................
12|.......................
13|-----------------------
"""

display.hline(0, 22, 160, color=0xffff)
display.hline(0, 87, 160, color=0xffff)
display.hline(0, 55, 160, color=0xffff)
display.vline(0, 22, 66, color=0xffff)
display.vline(160, 22, 66, color=0xffff)
display.vline(80, 22, 66, color=0xffff)

# endless loop
while(True):
    #print("oT: ", old_temp)
    #print("T: ", temp)
    if not temp == old_temp: # only delete old value and write new one if new sensor value is different from old one
        display.fill_rectangle(91, 35, 12, 8, 0) # delete old value by over drawing with a black rectangle
        bf.text(str(temp) + " øC", 91, 35, 0xfff) # put new value on the display (btw... øC will show on the display as °C)

    if not hum == old_hum:
        display.fill_rectangle(91, 67, 12, 8, 0)
        bf.text(str(hum) + " %", 91, 67, 0xfff)

    if not mf == old_mf:
        display.fill_rectangle(91, 130, 30, 8, 0)
        bf.text(str(mf), 91, 130, 0xfff)

    # store old sensor values for comparison purpose
    old_temp = temp
    old_hum = hum
    old_mf = mf
    
    # get new sensor values
    dht11sensor.measure()
    temp = dht11sensor.temperature()
    sleep(1)
    hum = dht11sensor.humidity()
    
    #get free memory value
    mf = gc.mem_free()
    
    # send temperature value to ADAFRUIT IO    
    try:
        client.publish(mqtt_feedname, bytes(str(temp), 'utf-8'), qos=0)
        #sleep(PUBLISH_PERIOD_IN_SEC)
        for i in range(1, 11):
            ledPin.value(0)
            sleep(0.1)
            ledPin.value(1)
            sleep(0.9)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
