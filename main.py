import board
# we use devkit N8R8
import math
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [ # There is 11 leds
    board.IO21,
    board.IO26, 
    board.IO47,
    board.IO33,
    board.IO34, 
    board.IO48,
    board.IO35,
    board.IO36, 
    board.IO37,
    board.IO38,
    board.IO39, 
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

maxvalue = 1.6; 
minvalue = 1.05; 

# main loop
while True:
    volume = microphone.value/20000; 
    # print(volume) 

    if volume > minvalue and volume < maxvalue: # 1.15 - 1.7 
        ledcount = volume - 1.15; 
        ledcount = math.floor(ledcount/0.05); 
        # print(math.floor(ledcount))
        lednumber = 0; 
        while lednumber <= ledcount:
            leds[lednumber].value = 1; 
            lednumber = lednumber + 1; 

    if volume > maxvalue:
        lednumber = 0; 
        while lednumber <= 10: 
            leds[lednumber].value = 1; 
            lednumber = lednumber + 1; 

    sleep(0.001)     

    lednumber = 10; 
    while lednumber >= 0:
            leds[lednumber].value = 0; 
            sleep(.04); 
            lednumber = lednumber - 1; 

    sleep(0.001)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
