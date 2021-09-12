# Miten tehdä pallo joka putoaa ruudun läpi?
import pygame

pygame.init()

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

painovoima_kiihtyvyys = 9.81

aika = 0.0 # kuinka paljon aikaa pelin alusta on kulunut
nopeus = 0.0
kierros_aika = 0.05 # kuinka kauan yksi kierros kestää? tämä on viive silmukan lopussa. pygame.time.wait()

while peli_kaynnissa:

    # pyyhitään edellinen ympyrä
    pygame.draw.circle(screen, musta, (x, y), sade)
    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False

    nopeuden_muutos = painovoima_kiihtyvyys * kierros_aika
    nopeus = nopeus + nopeuden_muutos

    matka = nopeus * aika

    y += matka

    pygame.draw.circle(screen, vihrea, (x, y), sade)
    print(f"aika: {aika:.2f}, pudottu matka {matka:.2f}, paikka {y:.2f}")

    aika += kierros_aika

    pygame.time.wait(int(kierros_aika*1000))
    pygame.display.flip()

pygame.quit()