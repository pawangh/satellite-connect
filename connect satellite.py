import pgzrun
import time
import random
WIDTH=800
HEIGHT=600
TITLE="connect satellite"
nolite=[]
for i in range(8):
    satel=Actor("satellite")
    satel.pos=(random.randint(100,700),random.randint(100,500))
    nolite.append(satel)
def draw():
    screen.blit("background",(0,0))
    satel.draw()
def update():
    pass
pgzrun.go()