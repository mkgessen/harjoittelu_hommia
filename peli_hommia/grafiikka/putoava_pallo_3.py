# Miten tehdä pallo_vihrea joka putoaa ruudun läpi?
# Pallo on tällä kertaa Sprite
import pygame

sininen = (0, 0, 255)
punainen = (255, 0, 0)
vihrea = (0, 255, 0)
musta = (0, 0, 0)
valkoinen = (255, 255, 255)


class Pallo(pygame.sprite.Sprite):
    def __init__(self, vari, x_paikka):
        super().__init__()
        self.pinta = pygame.Surface((50, 50))
        self.pinta.fill(musta)
        self.alue = self.pinta.get_rect()
        self.vari = vari
        pygame.draw.circle(self.pinta, vari, (25, 25), 20)
        self.alue.move_ip(x_paikka, 0)

    def siirra(self, x, y):
        self.alue.move_ip(x, y)


pygame.init()
clock = pygame.time.Clock()

# Luo näyttö
screen = pygame.display.set_mode([200, 1000])

# lopetettaan kun peli_kaynnissa = False
peli_kaynnissa = True

x = 100  # x aloituspaikka (keskellä)
y = 0  # y aloituspaikka (ruudun yläreuna)
sade = 20  # pallon säde

painovoima_kiihtyvyys = 9.81

aika = 0.0  # kuinka paljon aikaa pelin alusta on kulunut
nopeus = 0.0
kierros_aika = 0.05  # kuinka kauan yksi kierros kestää? tämä on viive silmukan lopussa. pygame.time.wait()

pallo_vihrea = Pallo(vihrea, 0)
pallo_punainen = Pallo(punainen, 50)
pallo_sininen = Pallo(sininen, 100)

while peli_kaynnissa:

    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False

    nopeuden_muutos = painovoima_kiihtyvyys * kierros_aika
    nopeus = nopeus + nopeuden_muutos

    matka = nopeus * aika

    y += matka
    pallo_vihrea.siirra(0, matka)
    pallo_punainen.siirra(0, matka)
    pallo_sininen.siirra(0, matka)
    screen.blit(pallo_vihrea.pinta, pallo_vihrea.alue)
    screen.blit(pallo_sininen.pinta, pallo_sininen.alue)
    screen.blit(pallo_punainen.pinta, pallo_punainen.alue)

    pygame.display.flip()
    clock.tick(30)
    print(f"aika: {aika:.2f}, pudottu matka {matka:.2f}, paikka {y:.2f}")

    aika += kierros_aika

    screen.fill(musta)

pygame.quit()