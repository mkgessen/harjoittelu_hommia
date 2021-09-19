# Miten tehdä pallo_vihrea joka pomppaa?
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
fps = 30.0
kierros_aika = 1.0/fps # kuinka kauan yksi kierros kestää? tämä on viive silmukan lopussa. pygame.time.wait()
suunta = 1
nopeus = 0.0
matka = 0.0
nollattu = True

while peli_kaynnissa:

    # pyyhitään edellinen ympyrä
    screen.fill(musta)

    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False

    nopeuden_muutos = kiihtyvyys * kierros_aika
    if suunta == 1:
        nopeus = nopeus + nopeuden_muutos
    else:
        nopeus = nopeus - nopeuden_muutos
    matka = nopeus * aika * suunta

    y += matka
    if y > 1000-sade and nollattu:
        suunta = suunta * -1
        nopeus = nopeus * 0.8
        nollattu = False
    else:
        pygame.draw.circle(screen, vihrea, (x, y), sade)
        nollattu = True

    aika += kierros_aika
    print(f"suunta: {suunta:.2f}, matkan muutos {matka:.2f}, paikka {y:.2f}, nopeus {nopeus:.2f}, dv {nopeuden_muutos:.2f}")

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()