import time
from sprite_handler import rudolphs
from sprite_handler import rudolph4


vel = 20


def leveldata():
    if len(rudolphs) < 1:
        rudolphs.append(rudolph4(1440,0))