# uPy ESP8266 D1mini Text to TFT ST7735
**This project allows you to show room temperature and humidity on a ST7735 display (160x128px) connected to an ESP8266 D1 mini**

</br>
<img src="https://i.imgur.com/EwXUg77.png">

It has been tested sucessfully with following setup:

* Windows 10 x64

* Micropython 1.9.4

* ESP8266 D1 mini  (other ESP8266 boards might work as well with some modifications depending on the model)

## Required hardware components:

    1 ST7735 TFT display
    1x ESP826 D1 mini
    1x DHT11 temperature & humidity sensor
          
## Pinout and schematic:

|Display Pin |ESP8266 Pin    |  |DHT11       |ESP8266      |
|------------|---------------|--|------------|-------------|
|GND         |GND            |  |VCC         |             |
|VCC         |3.3V           |  |            |             |
|SCK         |D5/CLK/GPIO14  |  |GND         |             |
|SDA         |D7/MOSI/GPIO13 |  |            |             |
|RES         |D3/GPIO0       |  |            |             |
|RS/DC/A0    |D0/GPIO16      |  |            |             |
|CS          |D8/CS/GPIO15   |  |            |             |
|LEDA        |3.3V           |  |            |             |
   
</br>
<img src="https://imgur.com/2dOCBLd.png" width="600">
Click to enlarge

## Bring the display to life

* [Arduino IDE](https://www.arduino.cc/en/software) need to be installed

* Connect the Arduino via USB to your PC
> Since the Arduino is placed inside my PC case I have myself created a cable to connect it to one of the internal USB headers directly on the mainboard so I don't need to route the cable to a USB port outside of the case. The temperature sensor I have fixed with a cable tie somewhere in the middle of the case - pictures will follow.

* Flash the KTY81-110_7segm.ino file to the Arduino NANO

* If everything has been setup correctly the temperature in your PC case will show up on the display

## Check the temperature on the serial line (COM port)

* As soon as the Arduino is powered up it will continously send the calculated resistance value and the temperature accordingly over the serial line via the USB the Arduino is connected to. It can be read off by connecting to the COM port with e.g. the Arduinos serial monitor, putty or any other serial monitor you're familiar with.
      
* The COM port your Arduino is connected to can easily be found by checking your Windows device manager or by looking in the Arduino IDE.
  
</br>
