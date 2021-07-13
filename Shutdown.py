# Simple script for shutting down the Raspberry Pi at the press of a button.
import RPi.GPIO as GPIO
import time
import os
import spidev

# Use the Broadcom SOC Pin numbers

# Setup the pin with internal pullups enabled and pin in reading mode.

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

 

# Our function on what to do when the button is pressed

def Shutdown(channel):
    bus = 0
    device = 0
    spi = spidev.SpiDev()
    spi.open(bus, device)
    spi.max_speed_hz = 100000
    spi.mode = 0b00
    #Stop Charging
    Stop_Charging_Command = [0x6,0x0,0x0,0xFE]
    spi.writebytes(Stop_Charging_Command)
    time.sleep(5)
    print("Shutting Down")
    os.system("sudo shutdown -h now")

 

# Add our function to execute when the button pressed event happens

GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

 

# Now wait!

while 1:

    time.sleep(1)