# Importieren u. initialisieren der Pygame-Bibliothek
import pygame
from pygame.locals import *


# Variablen/KONSTANTEN setzen
W, H = 800, 600
FPS  = 30
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GRAU    = ( 125,125,15)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self,xkoordinate,ykoordinate,speed):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bilder/biene.png')
        #self.image.fill(SCHWARZ)
        self.rect = self.image.get_rect()
        self.rect.x = xkoordinate
        self.rect.y = ykoordinate
        self.speed = speed
    def update(self):
        #self.rect.x += speed
        if self.rect.left > W:
            self.rect.right = 0
def main():
    pygame.init()
    player = Player(100,200,1)
    all_sprites.add(player)
    # Definieren und Öffnen eines neuen Fensters
    fenster = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Varroa Invaders")

    # Schleife Hauptprogramm
    spielaktiv = True
    while spielaktiv :
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            # Beenden bei [ESC] oder [X]
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                spielaktiv = False

        # Spiellogik

        # Spielfeld löschen
        all_sprites.update()
        #player.update(5)
        fenster.fill(GRAU)

        # Spielfeld/figuren zeichnen
        all_sprites.draw(fenster)

        
        # Fenster aktualisieren
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()