# Micropython - ESP8266 D1mini - DHT11 to ST7735 TFT
**This project allows you to show room temperature and humidity on an ST7735 TFT display (160x128px) connected to an ESP8266 D1 mini and visualize in a graph on WWW.IO.ADAFRUIT.COM**

</br>
<img src="https://imgur.com/kPmrGMm.jpg">

</br>
</br>

It has been tested sucessfully with following setup:

    Windows 10 x64
    Micropython 1.9.4
    ESP8266 D1 mini  (other ESP8266 boards might work as well with some modifications depending on the model)

## Required hardware components and setup at io.adafruit.com:

    1 ST7735 TFT display
    1x ESP826 D1 mini
    1x DHT11 temperature & humidity sensor
    1x 10K resistor
	
	Create an account at www.io.adafruit.com
	Create a feed in your account
	Add your account and feed data to the main.py file
          
## Pinout and schematic:

|Display Pin |ESP8266 Pin    |  |DHT11 Pin   |ESP8266 Pin  |
|------------|---------------|--|------------|-------------|
|GND         |GND            |  |VCC         |3.3V         |
|VCC         |3.3V           |  |Data        |D1/GPIO5     |
|SCK         |D5/CLK/GPIO14  |  |GND         |GND          |
|SDA         |D7/MOSI/GPIO13 |  |            |             |
|RES         |D3/GPIO0       |  |            |             |
|RS/DC/A0    |D0/GPIO16      |  |            |             |
|CS          |D8/CS/GPIO15   |  |            |             |
|LEDA        |3.3V           |  |            |             |
   
</br>
<img src="https://i.imgur.com/AekRgzC.jpg" width="600">
Click to enlarge

## Bring the display to life

Connect the ESP8266 via USB to your PC

Flash the following files to the ESP8266:

	st7735.py
	rgb.py
	bitmapfont.py
	font5x8.bin
	dht11-tft.py

On the micropython console type:

	import dht11-tft

If everything has been setup correctly the display should show temperature, humidity and the free memory of the ESP8266
