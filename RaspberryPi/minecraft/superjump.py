#!/usr/bin/python

from gpiozero import Button
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from signal import pause
mc = Minecraft.create()
tp = mc.player.setPos
button = Button(6)

def superJump():
    x, y, z = mc.player.getPos()
    if mc.getBlock(x, y-1, z) is not block.AIR.id:
        for n in range(1,21):
            x, y, z = mc.player.getPos()
            if button.is_pressed:
                tp(x, y+3, z)
        sleep(.001)

button.when_pressed = superJump

pause()
