#!/usr/bin/python

from gpiozero import LED, Button, Buzzer
from signal import pause

# Setup our LED, Button, and Buzzer
led = LED(19)
button = Button(6)
buzzer = Buzzer(17)

# Function we'll call on when_pressed event
def pressed(arg=None):
    led.on()
    buzzer.on()

# Function we'll call on when_released event
def released(arg=None):
    led.off()
    buzzer.off()

# Handle when_pressed event
button.when_pressed = pressed

# Handle when_released event
button.when_released = released

# Tell the user how to quit
print "Press Ctrl-C to exit"

# Pause and wait for butten events
pause()
