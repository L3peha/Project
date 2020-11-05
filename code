import pygame

pygame.init()

#size of findow, figures, outlines
Xsize=40
Osize=40
unitSize=50#with outlines
actualUnitSize=48
lineSize=1
n=15
player=2
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
mas = [[0] * (n+2) for i in range(n+2)]
for i in range(n+2):
    print(mas[i])
print('---------------------')

#a - number of unit 1 or 2
#x,y - coordinates
#xP,xY - offset of new unit from start
#b - quntity of found units
def check(a,x,y,xP,yP,b):
    if b == 1:
       if mas[x + 1][y + 1] == a:
              b+=1
              xP=1
              yP=1
              return check(a,x+xP,y+yP,xP,yP,b)
       if mas[x + 1][y] == a:
              b+=1
              xP=1
              yP=0
              return check(a,x+xP,y+yP,xP,yP,b)
       if mas[x][y + 1] == a:
              b+=1
              xP=0
              yP=1
              return check(a,x+xP,y+yP,xP,yP,b) 
       if mas[x + 1][y - 1] == a:
              b+=1
              xP=+1
              yP=-1
              return check(a,x+xP,y+yP,xP,yP,b)
    else :
       if mas[x + xP][y + yP] == a :
          b += 1
          if b < 5 :
             return check(a, x + xP, y + yP, xP, yP, b)
          if b >= 5 :
             return True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_focused():
                    Xpos=int(event.pos[0]/50)+1
                    Ypos=int(event.pos[1]/50)+1
                    if mas[Xpos][Ypos]==0:
                        if player==2:
                            pygame.draw.circle(screen, OColour, ((Xpos-1)*50+25,(Ypos-1)*50+25), 20, lineSize)
                            mas[Xpos][Ypos]=1
                            player=1
                            pygame.display.update()
                            print (Xpos, Ypos)
                            for i in range (11) :
                                for j in range (11) :
                                    if mas[i][j] != 0 :          #check returns xP yP and 0 1 - |;  1 1 - \; 1 -1 - /; 1 0 - -- 
                                        if check(1,i,j,0,0,1) :
                                            f2 = pygame.font.SysFont('serif', 54)
                                            text2 = f2.render("0 wins!", 0, (0, 180, 0))
                                            screen.blit(text2, (2*x/5, 2*y/5))
                                            pygame.display.update()
                                            pygame.time.wait(1000)
                                            running = False
                            print('------------')
                            for i in range(n+2):
                                print(mas[i])
                            print('---------------------')
                        else:
                            pygame.draw.line(screen, XColour, [(Xpos-1)*50+5,(Ypos-1)*50+5], [(Xpos-1)*50+45,(Ypos-1)*50+45])
                            pygame.draw.line(screen, XColour, [(Xpos-1)*50+45,(Ypos-1)*50+5], [(Xpos-1)*50+5,(Ypos-1)*50+45])
                            mas[Xpos][Ypos]=2
                            player=2
                            pygame.display.update()
                            print (Xpos, Ypos)
                            for i in range (11) :
                                for j in range (11) :
                                    if mas[i][j] != 0 :
                                        if check(2,i,j,0,0,1) :
                                            f2 = pygame.font.SysFont('serif', 54)
                                            text2 = f2.render("X wins!", 0, (0, 180, 0))
                                            screen.blit(text2, (2*x/5, 2*y/5))
                                            pygame.display.update()
                                            pygame.time.wait(1000)
                                            running = False
                            print('------------')
                            for i in range(n+2):
                                print(mas[i])
                            print('---------------------')


