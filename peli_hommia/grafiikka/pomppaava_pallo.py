# Miten tehdä pallo joka pomppaa?
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

painovoima_kiihtyvyys = 90.81
massa = 1 # kilogrammoina
voima = massa * painovoima_kiihtyvyys


aika = 0.0 # kuinka paljon aikaa pelin alusta on kulunut
kierros_aika = 0.05 # kuinka kauan yksi kierros kestää? tämä on viive silmukan lopussa. pygame.time.wait()
suunta = 1
nopeus = 0.0
vapaa_pudotus = True
matka = 0.0
while peli_kaynnissa:

    # pyyhitään edellinen ympyrä
    pygame.draw.circle(screen, musta, (x, y), sade)

    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False


    nopeuden_muutos = painovoima_kiihtyvyys * kierros_aika * suunta
    nopeus = nopeus + nopeuden_muutos

    paikan_muutos = nopeus * kierros_aika * suunta

    y += paikan_muutos
    if y > 1000-sade or y < 0:
        suunta = suunta * -1
    else:
        pygame.draw.circle(screen, vihrea, (x, y), sade)

    aika += kierros_aika
    print(f"aika: {aika:.2f}, matkan muutos {paikan_muutos:.2f}, paikka {y:.2f}, nopeus {nopeus:.2f}")

    pygame.time.wait(int(kierros_aika*1000))
    pygame.display.flip()

pygame.quit()