import time
from sprite_handler import rudolphs
from sprite_handler import rudolph4


vel = 15


def leveldata():
    if len(rudolphs) < 1:
        rudolphs.append(rudolph4(0,0))
        time.sleep(1581749919.0435092)
        rudolphs.append(rudolph4(0,0))
        time.sleep(1581749920.7113483)
        rudolphs.append(rudolph4(0,0))
        time.sleep(1581749922.5002692)
        rudolphs.append(rudolph4(0,0))
        time.sleep(1581749924.0106392)
        rudolphs.append(rudolph4(0,0))