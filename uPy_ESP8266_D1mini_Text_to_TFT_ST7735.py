from machine import Pin, SPI
from time import sleep
import st7735
import bitmapfont
import gc
from dht import DHT11

gc.enable()

# inits
display = st7735.ST7735R(SPI(1, baudrate=40000000), dc=Pin(16), cs=Pin(15), rst=Pin(0))

bf = bitmapfont.BitmapFont(128,160, display.pixel)
bf.init()

dht11sensor = DHT11(Pin(5))

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
display.hline(0, 22, 160, color=0xffff)
display.hline(0, 87, 160, color=0xffff)
display.hline(0, 55, 160, color=0xffff)
display.vline(0, 22, 66, color=0xffff)
display.vline(160, 22, 66, color=0xffff)
display.vline(80, 22, 66, color=0xffff)

# endless loop
while(True):
    if not temp == old_temp: # only delete old value and write new one if new sensor value is different from old one
        display.fill_rectangle(91, 67, 24, 8, 0) # delete old value by over drawing with a black rectangle
        bf.text(str(temp) + " øC", 91, 35, 0xfff) # put new value on the display (btw... øC will show on the display as °C)

    if not hum == old_hum:
        display.fill_rectangle(91, 67, 30, 8, 0)
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
    hum = dht11sensor.humidity()
    
    #get free memory value
    mf = gc.mem_free()
    
    sleep(2)
