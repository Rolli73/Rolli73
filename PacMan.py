import pygame
from pygame.locals import *

#from pygame_functions import *
BREITE = 800    
HOEHE  = 600
WEIS =(255,255,255)
FPS = 60
pygame.display.set_caption("Varroa Invaders")
clock = pygame.time.Clock()
fenster = pygame.display.set_mode([BREITE,HOEHE])
hintergrund = pygame.image.load("bilder/wiese.jpg")

class Player (pygame.sprite.Sprite):
    def __init__(self,datei):

        super().__init__()
        
        self.image = pygame.image.load(datei)
        self.rect = self.image.get_rect()
        
        
        
    
    def update(self,x,y):
        
        
        self.rect.center = (x,y)
        

            
        
        
            
       
def main():
    xkor = 200
    ykor = 200
    spielaktiv = True
    spieler = Player("Bilder/Daco50x49.png")
    spieler2 = Player("Bilder/Biene.png")
    
    spritesall = pygame.sprite.Group()
    spritesall.add(spieler2)
    player = pygame.sprite.GroupSingle(spieler)
    pygame.init()
    while spielaktiv:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                spielaktiv = False
            if event.type == pygame.MOUSEMOTION:
                spieler.rect.center = event.pos
        xkor +=1   

        
        fenster.blit(hintergrund,(0,0))
       
        spieler2.update(xkor,ykor)
        
        spritesall.draw(fenster)
        player.draw(fenster)
        

        pygame.display.flip()
    clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()          
