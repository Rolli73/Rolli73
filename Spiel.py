import pygame as pg
import math
import sys
import pygame_functions



pg.init()

Screen_width = 800
Screen_height = 600
Grau = 125,125,125
Weiss = 255,255,255
screen= pg.display.set_mode((Screen_width,Screen_height))
clock = pg.time.Clock()
pg.mouse.set_visible(True)
Hintergrund = pg.image.load("Bilder/wiese.jpg")


        


class  figur():
    def __init__(self,x,y,bildname):
        self.x = x
        self.y = y
        self.bildname = pg.image.load(bildname)



Fkreuz  = figur(100,100,"Bilder/Daco50x49.png")
Biene = figur(50,250,"Bilder/Biene.png")
Grösse = Fkreuz.bildname.get_rect()
print (Grösse.center[0])
print (Grösse.center[1])
Isrunning = True

while Isrunning:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                Isrunning = False
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
           
            Fkreuz.x,Fkreuz.y = event.pos
            
    #Spielelogik
                
    
    #Spielfeld löschen
    screen.fill(Grau)

   

    # Spielfeld/Figuren zeichnen
    screen.blit(Hintergrund,(0,0))
    screen.blit(Biene.bildname,(Biene.x,Biene.y))
    screen.blit(Fkreuz.bildname,(Fkreuz.x,Fkreuz.y))
    
    
    #Fenster aktualisieren
    pg.display.flip()

    # Refresh Zeit festlegen

    clock.tick(60)

pg.quit()

