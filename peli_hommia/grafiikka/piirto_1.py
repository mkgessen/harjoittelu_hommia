# Miten piirtä perusmuotoja?
# https://www.pygame.org/docs/ref/draw.html


# moduuli pygame.draw

# funktio               piirtää mitä?
# pygame.draw.rect      nelikulmion, muoto annetaan muodossa (vas yläkulma x, vas yläkulma y, leveys, pituus)
# pygame.draw.polygon   monikulmion, muoto annetaan listana x, y koordinaatteja
# pygame.draw.circle    ympyrän, muoto annetaan keskipisteen x, y ja säde
# pygame.draw.ellipse   soikion, muoto annetaan nelikulmiona johon ellipsin reunat osuu
# pygame.draw.arc       kaaren,  muoto annetaan nelikulmiona johon ellipsin reunat osuu + kaaren alku- ja loppukulma
# pygame.draw.line      viivan, muoto annetaan alku ja loppu pisteinä


from numpy import pi
import pygame
pygame.init()

def radiaaneiksi(asteet):
    return asteet * pi / 180.0

#          R, G, B
#          punainen, vihreä, sininen
#          pienin arvo on 0
#          suurin arvo on 255 (256 vaihtoehtoa eli 8-bittiä)

sininen = (0, 0, 255)
punainen = (255, 0, 0)
vihrea = (0, 255, 0)
musta = (0, 0, 0)
valkoinen = (255, 255, 255)

# Luo näyttö
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
peli_kaynnissa = True

while peli_kaynnissa:

    # Ikkuna suljettu?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            peli_kaynnissa = False

    # Tee ruudusta jonkun värinen. Muuten se on musta
    # screen.fill(valkoinen)

    # piirrä ympyrä
    keskipiste = (100, 30)
    sade = 20
    pygame.draw.circle(screen, vihrea, (10,20), sade)

    # piirrä viiva
    alkupiste = (100, 100)
    loppupiste = (200, 100)
    viivan_paksuus = 20
    pygame.draw.line(screen, sininen, alkupiste, loppupiste, viivan_paksuus)

    # piirrä nelikulmio
    paikka_x = 100
    paikka_y = 200
    korkeus = 100
    leveys = 200
    nelikulmio = pygame.Rect(paikka_x, paikka_y, leveys, korkeus)

    viivan_paksuus = 20
    pygame.draw.rect(screen, vihrea, nelikulmio)

    # piirrä soikio
    paikka_x = 100
    paikka_y = 400
    korkeus = 100
    leveys = 400
    nelikulmio = pygame.Rect(paikka_x, paikka_y, leveys, korkeus)

    viivan_paksuus = 20
    pygame.draw.ellipse(screen, punainen, nelikulmio)

    # piirrä kaari
    paikka_x = 100
    paikka_y = 600
    korkeus = 100
    leveys = 100
    nelikulmio = pygame.Rect(paikka_x, paikka_y, leveys, korkeus)

    viivan_paksuus = 3
    pygame.draw.arc(screen, sininen, nelikulmio, radiaaneiksi(90), radiaaneiksi(270), viivan_paksuus)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()