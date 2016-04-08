from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(19)


def my_func():
    print ("HERE")
    led.on()
    sleep(1)
    led.off()

button.when_pressed = my_func
#button.when_released = led.off

pause()
