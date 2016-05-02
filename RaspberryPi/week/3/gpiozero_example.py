from gpiozero import LED, Button, Buzzer

led = LED(19)
button = Button(6)
buzzer = Buzzer(17)

buzzer.on()
buzzer.off()

led.on()
led.off()

button.when_pressed = led.on
button.when_released = led.off
