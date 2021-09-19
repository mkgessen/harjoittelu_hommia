# Miten liikuttaa ympyrää näppäimillä?
# https://www.pygame.org/docs/ref/draw.html

import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, K_ESCAPE
pygame.init()

sininen = (0, 0, 255)
punainen = (255, 0, 0)
vihrea = (0, 255, 0)
musta = (0, 0, 0)
valkoinen = (255, 255, 255)

# Luo näyttö
screen = pygame.display.set_mode([1000, 1000])

# lopetettaan kun peli_kaynnissa = False
peli_kaynnissa = True

# paikka tulostetaan vain silloin kun se on muuttunut
# aluksi True, jotta paikka tulostuu heti "pelin" alussa
paikka_muuttunut = True

# alkupaikkana 0, 0 eli vasen yläkulma (jos meillä olisi grafiikkaa)
x = 100
y = 100

sade = 20

while peli_kaynnissa:

    # Ikkuna suljettu?
    for event in pygame.event.get():

        # jos tapahtuma oli näppäimen painaminen, niin tutkitaan mitä näppäintä on painettu
        # ollaan kiinnostuneita vain nuolista ja ESC:stä. Mikään muu näppäin ei tee tässä pelissä mitään
        if event.type == pygame.KEYDOWN:

            if event.key == K_UP:
                # painettu nuolta ylös
                y = y - 10
                paikka_muuttunut = True
            elif event.key == K_DOWN:
                # painettu nuolta alas
                y = y + 10
                paikka_muuttunut = True

            if event.key == K_LEFT:
                # painettu nuolta vasemmalle
                x = x - 10
                paikka_muuttunut = True
            elif event.key == K_RIGHT:
                # painettu nuolta oikealle
                x = x + 10
                paikka_muuttunut = True

            if event.key == K_ESCAPE:
                # painettu ESCiä
                peli_kaynnissa = False

        elif event.type == pygame.QUIT:
            peli_kaynnissa = False

    if paikka_muuttunut:
        screen.fill(musta)
        print(f"paikkani on {x, y}")
        # piirrä ympyrä
        pygame.draw.circle(screen, vihrea, (x, y), sade)
        # Flip the display
        pygame.display.flip()

        # mitä eri tapoja on päästä eroon edellisestä ympyrästä?
        paikka_muuttunut = False



# Done! Time to quit.
pygame.quit()