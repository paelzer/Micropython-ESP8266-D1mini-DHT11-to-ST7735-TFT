from machine import Pin, SPI
from time import sleep
import st7735
import bitmapfont

# DHT11 sensor related library
from dht import DHT11

display = st7735.ST7735R(SPI(1, baudrate=40000000), dc=Pin(16), cs=Pin(15), rst=Pin(0))

bf = bitmapfont.BitmapFont(160,128, display.pixel)
bf.init()

# sensor values initially 0
dht11sensor = DHT11(Pin(5))

#temp = dht11sensor.temperature()
#hum = dht11sensor.humidity()

temp = 0
hum = 0

# store old sensor values
oldTemp = temp
oldHum = hum

# name column x - position
nameCol = 7

# y - positions
tempRow = 30
humRow = 45

# x - position for sensor values
valCol = 80

# names for the sensor
nameTemp = "Temperatur:"
nameHum = "Humidity:"

# clear the display
display.fill(0)

# heading
bf.text("Some sensor values...", 0, 0, 0xffff)

# put sensor values names on the display
bf.text(nameTemp, nameCol, tempRow, 0xffff)
bf.text(nameHum, nameCol, humRow, 0xffff)

# draw a table
# display.h/vline(x, y, length, color)
display.hline(0,17, 160, color=0xffff)
display.hline(0,82, 160, color=0xffff)
display.vline(0,17, 66, color=0xffff)
display.vline(160,17, 66, color=0xffff)
display.vline(68,17, 66, color=0xffff)

# endless loop
while(True):
    if not temp == oldTemp: # only overwrite and delete row if new sensor value is different from old one
        bf.text(str(oldTemp), valCol, tempRow, 0x00) # delete row
        bf.text(str(temp), valCol, tempRow, 0xfff) # put new value on the display

    if not hum == oldHum:
        bf.text(str(oldHum), valCol, humRow, 0x00)
        bf.text(str(hum), valCol, humRow, 0xfff)

    # store old sensor values for overwrite purpose
    oldTemp = temp
    oldHum = hum
    
    # get new sensor values
    dht11sensor.measure()
    temp = dht11sensor.temperature()
    hum = dht11sensor.humidity()
    
    sleep(5)
