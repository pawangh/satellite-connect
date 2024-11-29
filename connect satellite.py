import pgzrun
import time
import random
WIDTH=800
HEIGHT=600
TITLE="connect satellite"
target=0
lines=[]
satellites=[]
for i in range(8):
    satel=Actor("satellite")
    satel.pos=(random.randint(100,700),random.randint(100,500))
    satellites.append(satel)
def draw():
    screen.blit("background",(0,0))
    satelnum=1
    for satel in satellites:
        satel.draw()
        screen.draw.text(str(satelnum),(satel.x,satel.y+10))
        satelnum=satelnum+1
    for line in lines:
        print(line)
        screen.draw.line(line[0],line[1],"white")
def on_mouse_down(pos):
    global lines,target
    if satellites[target].collidepoint(pos):
        if target > 0: 
            lines.append((satellites[target-1].pos,satellites[target].pos))
        target=target+1
    else:
        lines.clear()
        target=0

def update():
    pass
pgzrun.go()