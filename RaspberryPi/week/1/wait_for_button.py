from gpiozero import LED
from gpiozero import Button
from time import sleep

led = LED(17)
button = Button(19)

while True:
    #button.wait_for_release()
    button.wait_for_press()
    #print('You pushed me')
    if led.is_lit:
        print('Turning off')
        led.off()
    else:
        print('Turning on')
        led.on()
