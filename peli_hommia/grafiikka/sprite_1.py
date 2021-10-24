import pygame, sys
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, K_ESCAPE, K_a


class Hahmo(pygame.sprite.Sprite):
    def __init__(self, leveys, korkeus, paikka_x, paikka_y):
        super().__init__()
        #self.image = pygame.Surface([leveys, korkeus])
        #self.image.fill((255, 0, 0))
        self.image = pygame.image.load('sprite.png')
        self.rect = self.image.get_rect()
        # rect = rectangle eli suorakaide (neliö)
        self.rect.center = [paikka_x, paikka_y]

    # args = lista
    # kwargs = sanakirja (kw=keyword => avain)
    def update(self, *args, **kwargs) -> None:
        # käyttää vain kwargs ja 'x' ja 'y'

        alkup_x, alkup_y = self.rect.center
        x_siirto = 0
        y_siirto = 0

        if 'y' in kwargs:
            y_siirto = kwargs['y']
        if 'x' in kwargs:
            x_siirto = kwargs['x']

        self.rect.center = (alkup_x + x_siirto, alkup_y + y_siirto)


clock = pygame.time.Clock()
ruudun_koko = (1920, 1080) # leveys, korkeus
musta = (0, 0, 0)

tausta = pygame.Surface([1920, 1080])
tausta.fill((0,0,0))

ruutu = pygame.display.set_mode(ruudun_koko)
m = Hahmo(50, 50, 100, 100)
o = Hahmo(90, 50, 700, 200)

hahmo_ryhma = pygame.sprite.Group()
hahmo_ryhma.add(m)
hahmo_ryhma.add(o)

while True:
    for event in pygame.event.get():
        x, y = 0, 0
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = 0
            y = 0
            if event.key == K_UP:
                # painettu nuolta ylös
                y = -10

            elif event.key == K_DOWN:
                # painettu nuolta alas
                y = 10

            if event.key == K_LEFT:
                x = -10
            elif event.key == K_RIGHT:
                x = 10

        ruutu.blit(tausta, (0,0))
        hahmo_ryhma.update(x=x, y=y)
        hahmo_ryhma.draw(ruutu)
        pygame.display.flip()
        clock.tick(60)
