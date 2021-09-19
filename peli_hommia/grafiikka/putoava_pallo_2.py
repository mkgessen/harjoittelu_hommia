# Miten tehdä pallo_vihrea joka putoaa ruudun läpi?
# Tällä kertaa pallo_vihrea on piirrettynä omalle 'pinnalle' (Surface) ja se saadaan näkyviin screen.blit-komennolla
import pygame

pygame.init()
clock = pygame.time.Clock()

sininen = (0, 0, 255)
punainen = (255, 0, 0)
vihrea = (0, 255, 0)
musta = (0, 0, 0)
valkoinen = (255, 255, 255)

# Luo näyttö
screen = pygame.display.set_mode([200, 1000])

# lopetettaan kun peli_kaynnissa = False
peli_kaynnissa = True

x = 100 # x aloituspaikka (keskellä)
y = 0 # y aloituspaikka (ruudun yläreuna)
sade = 20  # pallon säde

kiihtyvyys = 10.0

aika = 0.0 # kuinka paljon aikaa pelin alusta on kulunut
nopeus = 0.0
fps = 30.0
kierros_aika = 1 / fps # kuinka kauan yksi kierros kestää?

pinta = pygame.Surface((50, 50))
pinta.fill(musta)
pygame.draw.circle(pinta, vihrea, (25, 25), sade)

while peli_kaynnissa:
    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False

    nopeuden_muutos = kiihtyvyys * kierros_aika
    nopeus = nopeus + nopeuden_muutos

    matka = nopeus * aika

    y += matka

    screen.blit(pinta, (x, y))
    pygame.display.flip()
    print(f"aika: {aika:.2f}, pudottu matka {matka:.2f}, paikka {y:.2f}")

    aika += kierros_aika


    clock.tick(fps)
    screen.fill(musta)


pygame.quit()