import pygame as pg


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAU = 125,125,125
WEISS = 255,255,255


        



class figur(pg.sprite.Sprite):
    def __init__(self,bild_dateipfad,x,y):
      # self.image = pg.Surface([50,50])
      
       self.image = pg.image.load(bild_dateipfad)
       self.rect = self.image.get_rect(center=(x,x))
       
    




def main():
    pg.init()

    screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pg.display.set_caption("MOORHUHN")
    clock = pg.time.Clock()
    #pg.mouse.set_visible(False)

    hintergrund = pg.image.load("Bilder/wiese.jpg")
    fadenkreuz  = figur("Bilder/Daco50x49.png",100,100)
    biene   = figur("Bilder/Biene.png",50,250)
    
    Isrunning = True
    while Isrunning:
        for event in pg.event.get():
            if (
                event.type == pg.QUIT 
                or event.type == pg.KEYDOWN 
                and event.key == pg.K_ESCAPE
                ):
                    Isrunning = False
            
            if event.type == pg.MOUSEMOTION:
                fadenkreuz.rect.center = event.pos

            if pg.sprite.collide_circle_ratio(0.3)(fadenkreuz,biene):
                
                Isrunning = False
            else:
                Isrunning = True
        #Spielelogik
                    
        
        #Spielfeld löschen
        #screen.fill(Grau)

    

        # Spielfeld/Figuren zeichnen
        screen.blit(hintergrund,(0,0))
        screen.blit(biene.image,biene.rect)
        screen.blit(fadenkreuz.image, fadenkreuz.rect)
       
        
        #Fenster aktualisieren
        pg.display.flip()

        # Refresh Zeit festlegen

        clock.tick(60)
    pg.quit()




if __name__ == "__main__":
    main()