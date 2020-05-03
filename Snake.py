# Importieren u. initialisieren der Pygame-Bibliothek
import pygame
from pygame.locals import *
pygame.init()
Multiplikator = 20
# Variablen/KONSTANTEN setzen
W, H = 40*Multiplikator, 30*Multiplikator
FPS  = 60
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GRAU    = ( 125, 125, 125)
# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W, H))
pygame.display.set_caption("Titel für Fensterkopf")
clock = pygame.time.Clock()
koerper = [9,10]
koerperx = 0
koerpery = 0

def korrektur(zahl):
    zahl *=Multiplikator
    return zahl

def kopfzeichnen(x,y):
     pygame.draw.ellipse(fenster,WEISS,(korrektur(x),korrektur(y),korrektur(1),korrektur(1)))
  
def koerperzeichnen(x,y):
    koerper [0] = x
    koerper [1] = y
    pygame.draw.ellipse(fenster,SCHWARZ,(korrektur(koerper[0]),korrektur(koerper[1]),korrektur(1),korrektur(1)))
# Schleife Hauptprogramm
def main():
    
    x = 10 
    y = 10
    while True:
        
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            # Beenden bei [ESC] oder [X]
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
            if event.type == KEYDOWN :
                if event.key == K_RIGHT:
                    
                    x += 1
                if event.key == K_LEFT:
                    
                    x -= 1
                if event.key == K_UP:
                    
                    y -= 1
                if event.key == K_DOWN:
                    
                    y += 1
        
        koerperx [0] = x
        koerpery [1] = y
                  
        # Spiellogik
        
        
        # Spielfeld löschen
        fenster.fill(GRAU)

        # Spielfeld/figuren zeichnen
        kopfzeichnen(x,y)
        koerperzeichnen(koerper[0],koerper[1])
        print(koerper)
        # Fenster aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
if __name__ == "__main__":
    main()