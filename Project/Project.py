import pygame
import os

pygame.init()

#size of findow, figures, outlines
Xsize=40
Osize=40
unitSize=50#with outlines
actualUnitSize=48
lineSize=1
n=15
x=int(n*unitSize+lineSize)
y=int(n*unitSize+lineSize)
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Крестики нолики')


#Colours of figures
backGroundColour = (255,255,230)
linesColour = (0,255,255)
XColour = (0,0,0)
OColour = (0,0,255)

#background
screen.fill(backGroundColour)
for i in range(n):
    for j in range(n):
        pygame.draw.rect(screen,linesColour,(i*unitSize+lineSize,j*unitSize+lineSize,unitSize,unitSize),lineSize)
pygame.draw.rect(screen,(0,0,0),(0,0,x-1,y-1),2*lineSize)

pygame.display.flip()

#pole in mas 0-nothing 1-x 2-o
mas = [[0] * n for i in range(n)]
for i in range(n):
    print(mas[i])





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_focused():
                    pygame.draw.circle(screen, OColour, event.pos, 20, lineSize)
                    pygame.display.update()