import pygame as pg
import math
import sys
import pygame_functions



pg.init()

Screen_width = 800
Screen_height = 600
Grau = 125,125,125
srcreen= pg.display.set_mode((Screen_width,Screen_height))
clock = pg.time.Clock()



        

FigurBild= pg.image.load("Bilder/Daco.png")
Raumschiff = pg.transform.scale(FigurBild,(50,50))


Isrunning = True

while Isrunning:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                Isrunning = False
    
    #Spielelogik
                
    
    #Spielfeld löschen
    srcreen.fill(Grau)

   

    # Spielfeld/Figuren zeichnen
    
    srcreen.blit(Raumschiff,(200,200))
   
    #Fenster aktualisieren
    pg.display.flip()

    # Refresh Zeit festlegen

    clock.tick(60)

pg.quit()

