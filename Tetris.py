import pygame as pg
from dataclasses import dataclass

BREITE    = 400
SPALTEN   = 10
ZEILEN    = 20
ABSTAND   = BREITE // SPALTEN
HOEHE     = ABSTAND * ZEILEN
GRID =[0] * SPALTEN *ZEILEN
SCREEN = pg.display.set_mode([BREITE, HOEHE])
BILDER =[]
for n in range (8):
    BILDER.append(pg.transform.scale(
        pg.image.load(f'bilder/Teil_11_tt3_{n}.gif'),(ABSTAND,ABSTAND)))
TETROMINOES = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0],
               [0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0]]

@dataclass
class Tetrominoe():
    tet : list
    zeile :  int = 0
    spalte : int = 3
    def show(self):
        for n, farbe in enumerate(self.tet):
            if farbe > 0:
                y = (self.zeile + n // 4) * ABSTAND
                x = (self.spalte + n % 4) * ABSTAND
                SCREEN.blit(BILDER[farbe], (x, y))


        
def main():
    pg.init()
    figur = Tetrominoe(TETROMINOES[6])

    spielaktiv = True
    while spielaktiv:
        for event in pg.event.get():
            if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
                spielaktiv = False
        SCREEN.fill((0,0,0))
        figur.show()
        
        for n, farbe in enumerate(GRID):
            if farbe > 0:
                x = n % SPALTEN * ABSTAND
                y = n // SPALTEN * ABSTAND
                SCREEN.blit(BILDER[farbe],(x,y))
        pg.display.flip()         
    pg.quit()

if __name__ == "__main__":
    main()          