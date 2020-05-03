import pygame,sys,time,random
from pygame.locals import *

ORANGE  = (255,190,0)
WEISS   = (255,255,255)
SCHWARZ = (0,0,0)
GRAU    = (125,125,125) 
MULTIPLIKATOR = 20
fenster = pygame.display.set_mode((20*MULTIPLIKATOR,29*MULTIPLIKATOR))
fenster.fill(GRAU)
#Spielball Variablen
ball_x = random.randint(3,16)
ball_y = 23
ball_x_richtung = 1
ball_y_richtung = -1
ball_x_alt = 0
ball_y_alt = 0
spiel_figur_1_x =10
spiel_figur_1_y =25
spiel_figur_1_x_alt = 0
spiel_figur_1_y_alt = 0
spiel_figur_richtung = 0
spiel_figur_1_breite = 6
# Titel für Fensterkopf
pygame.display.set_caption("Breakout in Python")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

#Spielfeld
karte=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

#Korrekturfaktor berechnen
def kor(zahl):
    zahl = zahl *MULTIPLIKATOR
    return zahl

#Spielelemente
def element_zeichnen(spalte,reihe):
    pygame.draw.rect(fenster,ORANGE,(kor(spalte)+1,kor(reihe)+1,kor(1)-1,kor(1)-1))

def element_löschen(spalte,reihe):
    pygame.draw.rect(fenster,GRAU,(kor(spalte),kor(reihe),kor(1),kor(1)))

#Spielball zeichnen
def ball_zeichnen(x,y):
    pygame.draw.ellipse(fenster,SCHWARZ,(kor(x),kor(y),kor(1),kor(1)))

#Schläger 
def spiel_figur_1(x):
    pygame.draw.rect(fenster,SCHWARZ,(kor(x),kor(y),kor(spiel_figur_1_breite),kor(1)))

def spiel_figur_loeschen(x):
    pygame.draw.rect(fenster,GRAU,(kor(x),kor(y),kor(spiel_figur_1_breite),kor(1)))

#Ausgabe Spielfeld Karte
for x in range (0,20):
    for y in range (0,27):
        if karte[y][x] !=0:
            element_zeichnen(x,y)






# Schleife Hauptprogramm
naechsterschritt = False

while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat beendet")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Nächster Schritt",ball_y_richtung)
            naechsterschritt = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spiel_figur_richtung = -1
            if event.key == pygame.K_RIGHT:
                spiel_figur_richtung = 1
    #Spielelogik
    if ball_x <= 0:
        ball_x_richtung = 1
    if ball_x >= 19:
        ball_x_richtung = -1
    if ball_y <= 0:
        ball_y_richtung = 1
    if ball_y >= 28:
        ball_y_richtung = -1
    if (spiel_figur_1_x == 0 and spiel_figur_richtung ==-1):
        spiel_figur_richtung = 0
    if (spiel_figur_1_x ==17 and spiel_figur_richtung == 1):
        spiel_figur_richtung = 0



    if ball_y_richtung == -1:
        # Ball ist in Aufwärtsbewegung
        # genau darüber ein Mauerstein?
        if karte[ball_y-1][ball_x] != 0:
            print("trifft Mauerstein oberhalb")
            # Mauerstein wird gelöscht von Bildschirm
            element_löschen(ball_x, ball_y-1)
            # Mauerstein wird gelöscht aus Liste karte
            karte[ball_y-1][ball_x] = 0
            ball_y_richtung = 1
        else:
            if ball_x_richtung == 1:
                if karte[ball_y-1][ball_x+1] != 0:
                    print('trifft Mauerstein rechts oben')
                    element_löschen(ball_x+1,ball_y-1)
                    karte[ball_y-1][ball_x+1] =0
                    ball_y_richtung = 1
                    ball_x_richtung = -1
            else:
                # Ball bewegt sich nach links
                if karte[ball_y-1][ball_x-1] != 0:
                    print("trifft Mauerstein links oberhalb")
                    # Mauerstein wird gelöscht von Bildschirm
                    element_löschen(ball_x-1, ball_y-1)
                    # Mauerstein wird gelöscht aus Liste karte
                    karte[ball_y-1][ball_x-1] = 0
                    ball_y_richtung = 1
                    # trifft auf Ecke, also gleich Richtung zurück
                    ball_x_richtung = +1

    if ball_y == 25 and ball_y_richtung == 1:
        if ball_x_richtung == 1:
            if ball_x+1 >= spiel_figur_1_x and ball_x+1 <= spiel_figur_1_x+spiel_figur_1_breite:
             ball_y_richtung =-1
        
        if ball_x_richtung ==-1:
            if ball_x-1 >= spiel_figur_1_x and ball_x-1 <= spiel_figur_1_x+spiel_figur_1_breite:
                ball_y_richtung =-1
    spiel_figur_loeschen(spiel_figur_1_x_alt)                
    spiel_figur_1(spiel_figur_1_x)
    # Siegbedingung erfüllt?
    mauersteine = 0
    for i in range(len(karte)):
        for j in range(len(karte[i])):
            if karte[i][j] == 1:
                mauersteine = mauersteine + 1
    if mauersteine > 1:
            print("noch sind Mauersteine ", mauersteine ," da")
    else:
            # gewonnen, alle Mauersteine sind weg
            # Ball wird eingefroren
            ball_x_richtung = 0
            ball_y_richtung = 0
            # Meldung für Sieg
            print("Gewonnen - herzlichen Glückwunsch") 
   
    #if naechsterschritt == True:   
    ball_x_alt = ball_x
    ball_y_alt = ball_y
    ball_x += ball_x_richtung
    ball_y += ball_y_richtung
    spiel_figur_1_x_alt = spiel_figur_1_x
    spiel_figur_1_x += spiel_figur_richtung

   
   
   # naechsterschritt= False
   
    element_löschen(ball_x_alt,ball_y_alt)
    ball_zeichnen(ball_x,ball_y)
    
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(10)

pygame.quit()