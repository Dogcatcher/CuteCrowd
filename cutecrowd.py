# Cute Crowd

import pygame, sys, numpy as np
from pygame.locals import *
from random import random,randint

pygame.init()
FPS=60
screenHeight=800
screenWidth=800
fpsClock=pygame.time.Clock()
SCREEN=pygame.display.set_mode((screenHeight,screenWidth),0,32)

grid=np.zeros((9,9),dtype=np.int)
crowd=[None]*9

SELECTOR=0
BOY=1
CATGIRL=2
HORNGIRL=3
PINKGIRL=4
PRINCESS=5
KEY=6
ENEMYBUG=7
STAR=8
iPath='PlanetCuteSmall\\'
crowd[SELECTOR]=pygame.image.load(iPath+'Selector.png')
crowd[BOY]=pygame.image.load(iPath+'Character Boy.png')
crowd[CATGIRL]=pygame.image.load(iPath+'Character Cat Girl.png')
crowd[HORNGIRL]=pygame.image.load(iPath+'Character Horn Girl.png')
crowd[PINKGIRL]=pygame.image.load(iPath+'Character Pink Girl.png')
crowd[PRINCESS]=pygame.image.load(iPath+'Character Princess Girl.png')
crowd[KEY]=pygame.image.load(iPath+'Key.png')
crowd[ENEMYBUG]=pygame.image.load(iPath+'Enemy Bug.png')
crowd[STAR]=pygame.image.load(iPath+'Star.png')

block=[None]*2
DIRTBLOCK=0
WATERBLOCK=1
block[DIRTBLOCK]=pygame.image.load(iPath+'Dirt Block.png')
block[WATERBLOCK]=pygame.image.load(iPath+'Water Block.png')

LEFT=1

width=50
height=40

def seedLevel():
    for x in range(0,9):
        for y in range(0,9):
            grid[x,y]=randint(1,5)
            
def drawScreen(x1,x2):
    print("passed x1:{0} x2:{1}".format(x1,x2)) 
    if (x1 > x2):
        print("swapping")
        x1,x2 = x2,x1
    print("drawing {0} to {1}".format(x1,x2))
    x2+=1
    for x in range(x1,x2):
        for y in range(0,9):
            SCREEN.blit(block[DIRTBLOCK],(x*width,(height/2)+y*height))
    
    for x in range(x1,x2):
        for y in range(0,9):
            SCREEN.blit(crowd[grid[x,y]],(x*width,y*height))
    pygame.display.flip()

def processGrid(x1,y1,x2,y2):
    if (x1 > x2):
        x1,x2=x2,x1
    if (y1 > y2):
        y1,y2=y2,y1
    x1-=2
    if (x1 < 0):
        x1=0
    x2+=2
    if (x2 > 8):
        x2=8
    y1-=2
    if (y1 < 0):
        y1=0
    y2+=2
    if (y2 > 8):
        y2=8    
    print("Checking columns {0} to {1}".format(x1,x2))
    print("Checking rows    {0} to {1}".format(y1,y2))
    
    return True

seedLevel()
drawScreen(0,8)
processGrid(0,0,8,8)
a=b=c=d=0
while True:
    for event in pygame.event.get():
        
        if (event.type == MOUSEBUTTONDOWN):
            (a,b)= pygame.mouse.get_pos()
            (a,b) = (int(a/width),int(b/height)-1)
            print("down {0},{1}".format(a,b))
        elif (event.type == MOUSEBUTTONUP):
            (c,d)= pygame.mouse.get_pos()
            (c,d) = (int(c/width),int(d/height)-1)
            print("up {0},{1}".format(c,d))
            if ((abs(a-c) == 1) and (abs(b-d) == 0)) or ((abs(a-c) == 0) and (abs(b-d) == 1)):
                print("swapping {0},{1} and {2},{3}".format(a,b,c,d))
                e=grid[a,b]
                grid[a,b]=grid[c,d]
                grid[c,d]=e
                drawScreen(a,c)
                processGrid(a,b,c,d)

        elif (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
    fpsClock.tick(FPS)    
    pygame.display.set_caption("FPS {0}".format(int(fpsClock.get_fps())))
