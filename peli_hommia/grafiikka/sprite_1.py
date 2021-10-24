import pygame, sys
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, K_ESCAPE, K_a


class Hahmo(pygame.sprite.Sprite):
    def __init__(self, leveys, korkeus, paikka_x, paikka_y):
        super().__init__()
        self.image = pygame.Surface([leveys, korkeus])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = [paikka_x, paikka_y]

    def update(self, *args, **kwargs) -> None:
        x, y = self.rect.center
        x_siirto, y_siirto = 0, 0
        if 'y' in kwargs:
            y_siirto = kwargs['y']
        if 'x' in kwargs:
            x_siirto = kwargs['x']

        self.rect.center = (x + x_siirto, y + y_siirto)


clock = pygame.time.Clock()
ruudun_koko = (1920, 1080) # leveys, korkeus
musta = (0, 0, 0)

tausta = pygame.Surface([1920, 1080])
tausta.fill((0,0,0))

ruutu = pygame.display.set_mode(ruudun_koko)

m = Hahmo(50, 50, 100, 100)

minun_ryhma = pygame.sprite.Group()
minun_ryhma.add(m)

while True:
    for event in pygame.event.get():
        x, y = 0, 0
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x, y = 0, 0
            if event.key == K_UP:
                # painettu nuolta ylös
                y = 10

            elif event.key == K_DOWN:
                # painettu nuolta alas
                y = -10

        pygame.display.flip()
        ruutu.blit(tausta, (0,0))
        minun_ryhma.draw(ruutu)
        minun_ryhma.update(x=x, y=y)
        clock.tick(60)
