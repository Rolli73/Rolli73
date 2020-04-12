import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAU = (125, 125, 125)
WEISS = (255, 255, 255)

#
# FIXME Das sieht nach einer Neuerfindung des Rades `pygame.sprite.Sprite` aus.
#
class Figur:
    def __init__(self, x, y, bild_dateipfad):
        self.image = pygame.image.load(bild_dateipfad)
        self.rect = self.image.get_rect(center=(x, y))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("MOORHUHN")
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    hintergrund = pygame.image.load("Bilder/wiese.jpg")

    fadenkreuz = Figur(100, 100, "Bilder/Daco50x49.png")
    biene = Figur(50, 250, "Bilder/Biene.png")

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
               ):
                is_running = False
            if event.type == pygame.MOUSEMOTION:
                fadenkreuz.rect.center = event.pos
        #
        # TODO Deckt `hintergrund` nicht den gesamten `screen` ab? Dann wäre
        # das vorherige einfarbige füllen überflüssig.
        #
        #screen.fill(GRAU)
        screen.blit(hintergrund, (0, 0))
        screen.blit(biene.image, biene.rect)
        screen.blit(fadenkreuz.image, fadenkreuz.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()