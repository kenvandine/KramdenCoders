from mcpi.minecraft import Minecraft
from time import sleep
from gpiozero import LED, Buzzer, Button

led = LED(19)
buzzer = Buzzer(17)
button = Button(6)

x1, y1, z1 = 24, 10, -38
x2, y2, z2 = 8, 7, -35
def teleport(foo=None):
    mc.postToChat("Teleporting!")
    mc.player.setPos(x2,y2,z2)


mc = Minecraft.create()
teleport()
button.when_pressed = teleport

while True:
    x = round(mc.player.getPos().x)
    y = round(mc.player.getPos().y)
    z = round(mc.player.getPos().z)

    sleep(1)
    if (x, y, z) == (x1, y1, z1):
        mc.postToChat("Teleporting!")
        mc.player.setPos(x2,y2,z2)
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()
