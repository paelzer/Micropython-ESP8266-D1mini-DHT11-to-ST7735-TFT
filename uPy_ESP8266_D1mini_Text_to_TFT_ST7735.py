from machine import Pin, SPI
from time import sleep
import st7735
import bitmapfont

display = st7735.ST7735R(SPI(1, baudrate=40000000), dc=Pin(16), cs=Pin(15), rst=Pin(0))

bf = bitmapfont.BitmapFont(160,128, display.pixel)
bf.init()

# sensor values initially 0
x = 0
y = 0
z = 0

# store old sensor values
oldX = x
oldY = y
oldZ = z

# name column x - position
nameCol = 7

# y - positions
xRow = 30
yRow = 45
zRow = 60

# x - position for sensor values
valCol = 80

# names for the sensor
xName = "Sensor 1:"
yName = "Sensor 2:"
zName = "Sensor 3:"

# clear the display
display.fill(0)

# heading
bf.text("Some sensor values...", 0, 0, 0xffff)

# put sensor values names on the display
bf.text(xName, nameCol, xRow, 0xffff)
bf.text(yName, nameCol, yRow, 0xffff)
bf.text(zName, nameCol, zRow, 0xffff)

# draw a table
# display.h/vline(x, y, length, color)
display.hline(0,17, 160, color=0xffff)
display.hline(0,82, 160, color=0xffff)
display.vline(0,17, 66, color=0xffff)
display.vline(160,17, 66, color=0xffff)
display.vline(68,17, 66, color=0xffff)

# endless loop
while(True):
    if not x == oldX: # only overwrite and delete row if new sensor value is different from old one
        bf.text(str(oldX), valCol, xRow, 0x00) # delete row
        bf.text(str(x), valCol, xRow, 0xfff) # put new value on the display

    if not y == oldY:
        bf.text(str(oldY), valCol, yRow, 0x00)
        bf.text(str(y), valCol, yRow, 0xfff)

    if not z == oldZ:
        bf.text(str(oldZ), valCol, zRow, 0x00)
        bf.text(str(z), valCol, zRow, 0xfff)
    
    # store old sensor values for overwrite purpose
    oldX = x
    oldY = y
    oldZ = z
    
    # fake sensor values changes (could be replaced by real sensor readings)
    x += 1
    y += 5
    z += 7
    
    sleep(1)
