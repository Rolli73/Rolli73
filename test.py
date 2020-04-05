
import math
import sys
import pygame_functions
import pygame as pg
pg.init()

Screen_width = 800
Screen_height = 600
Grau = 125,125,125
srcreen= pg.display.set_mode((Screen_width,Screen_height))
clock = pg.time.Clock()

class Figur():
    def __init__(self,x_gr,y_gr,x_pos,y_pos):
        self.x_gr = x_gr
        self.y_gr = y_gr
        self.x_pos = x_pos
        self.y_pos = y_pos
        return srcreen.blit((self.x_pos,self.y_pos))

        FigurBild= pg.image.load("Daco.png")
Raumschiff = pg.transform.scale(FigurBild,(50,50))
Ship = Figur(50,50,100,150)

Isrunning = True

while Isrunning:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                Isrunning = False
    
    #Spielelogik
                
    
    #Spielfeld löschen
    srcreen.fill(Grau)

   

    # Spielfeld/Figuren zeichnen
    Feind = Figur(50,50,150,150)
    srcreen.blit(Raumschiff,(200,200))
    Figur(Feind)
    #Fenster aktualisieren
    pg.display.flip()

    # Refresh Zeit festlegen

    clock.tick(60)

pg.quit()