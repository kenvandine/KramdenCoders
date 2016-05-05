#!/usr/bin/python

from mcpi.minecraft import Minecraft
from time import sleep
from gpiozero import LED, Buzzer, Button

# Setup LED, Buzzer and Button
led = LED(19)
buzzer = Buzzer(17)
button = Button(6)

# Location of the portal
x1, y1, z1 = 24, 10, -38

# Location we want to teleport the player to
x2, y2, z2 = 8, 7, -35

# Teleport the player to defined location
def teleport(foo=None):
    mc.postToChat("Teleporting!")
    mc.player.setPos(x2,y2,z2)

# Connect to the currently running Minecraft game
mc = Minecraft.create()

# Teleport the player to a location near the portal
teleport()

# Handle the when_pressed button event
button.when_pressed = teleport

while True:
    x = round(mc.player.getPos().x)
    y = round(mc.player.getPos().y)
    z = round(mc.player.getPos().z)

    sleep(1)
    # Check to see if the player is in the portal
    if (x, y, z) == (x1, y1, z1):
        mc.postToChat("Teleporting!")
        mc.player.setPos(x2,y2,z2)
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()
