# PC case temperature on a 4-digit 7-segment display
**This project allows you to show your PC case temperature on a 4 digit 7 segment display connected to an Arduino NANO**

**Not that it's really neccessary to have this... but I think it looks cool anyway :-)**

</br>
<img src="https://i.imgur.com/EwXUg77.png">

It has been tested sucessfully with following setup:

* Windows 10 x64

* Arduino IDE 1.8.16

* Arduino NANO (other Arduino boards work as well with some modifications depending on the model)

## Required hardware components:

    7 segment display with 4 digits (common anode type)
    1x 8bit shift register 74HC595
    1x Resistor 3.3K Ohm
    8x Resistor 220 Ohm
    KTY81 110 temperature sensor
    Arduino NANO
      
## Pinout and schematic:

|74HC595 Pin |Display Pin |  |74HC595 Pin |Arduino Pin  |  |Arduino NANO|Display Pin|   |KTY81-110 Pin|Arduino Pin|
|------------|------------|--|------------|-------------|--|------------|-----------|---|-------------|-----------|        
|Q0          |11          |  |MR	  |D12          |  |D2          |12         |   |1            |A1         |       
|Q1          |1           |  |SH_CP       |D6           |  |D3          |9          |   |2            |5V         |       
|Q2          |2           |  |ST_CP       |D7           |  |D4          |8          |   |             |           |       
|Q3          |3           |  |DS	  |D8           |  |D5          |6          |   |             |           |       
|Q4          |4           |  |OE          |GND          |  |            |           |   |             |           |       
|Q5          |5           |  |VCC         |5V           |  |            |           |   |             |           |       
|Q6          |7           |  |GND         |GND          |  |            |           |   |             |           |       
|Q7          |10          |  |            |             |  |            |           |   |             |           |
	    
</br>
<img src="https://i.imgur.com/jWa8qOf.png" width="600">
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
