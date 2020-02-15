import time
from sprite_handler import rudolphs
from sprite_handler import rudolph4


vel = 15


def leveldata():
    if len(rudolphs) < 1:
        #rudolphs.append(rudolph4(0,0))
        rudolphs.append(rudolph4(240,0))
        #rudolphs.append(rudolph4(480,0))
        rudolphs.append(rudolph4(720,0))
        #rudolphs.append(rudolph4(960,0))
        #rudolphs.append(rudolph4(1200,0))
        #rudolphs.append(rudolph4(1440,0))
        #rudolphs.append(rudolph4(1680,0))