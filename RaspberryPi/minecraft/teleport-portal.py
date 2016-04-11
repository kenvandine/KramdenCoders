from mcpi.minecraft import Minecraft
from time import sleep
from gpiozero import LED, Buzzer

led = LED(6)
buzzer = Buzzer(17)

mc = Minecraft.create()
x1, y1, z1 = 24, 10, -38
x2, y2, z2 = 8, 7, -35
mc.player.setPos(x2,y2,z2)
#print (x1, y1, z1)
while True:
    x = round(mc.player.getPos().x)
    y = round(mc.player.getPos().y)
    z = round(mc.player.getPos().z)

    sleep(1)
    #print (x, y, z)
    if (x, y, z) == (x1, y1, z1):
        mc.postToChat("Teleporting!")
        mc.player.setPos(x2,y2,z2)
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()
