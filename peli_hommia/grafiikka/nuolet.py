# Miten saadaan jotain tapahtumaan kun näppäimiä painetaan?


import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, K_ESCAPE
pygame.init()
screen = pygame.display.set_mode([1000, 1000])

# lopetettaan kun peli_kaynnissa = False
peli_kaynnissa = True

# paikka tulostetaan vain silloin kun se on muuttunut
# aluksi True, jotta paikka tulostuu heti "pelin" alussa
paikka_muuttunut = True

# alkupaikkana 0, 0 eli vasen yläkulma (jos meillä olisi grafiikkaa)
x = 0
y = 0

while peli_kaynnissa:

    # tutkitaan onko uusia tapahtumia
    for event in pygame.event.get():

        # jos tapahtuma oli näppäimen painaminen, niin tutkitaan mitä näppäintä on painettu
        # ollaan kiinnostuneita vain nuolista ja ESC:stä. Mikään muu näppäin ei tee tässä pelissä mitään
        if event.type == pygame.KEYDOWN:

            if event.key == K_UP:
                # painettu nuolta ylös
                y = y + 1
                paikka_muuttunut = True
            elif event.key == K_DOWN:
                # painettu nuolta alas
                y = y - 1
                paikka_muuttunut = True

            if event.key == K_LEFT:
                # painettu nuolta vasemmalle
                x = x - 1
                paikka_muuttunut = True
            elif event.key == K_RIGHT:
                # painettu nuolta oikealle
                x = x + 1
                paikka_muuttunut = True

            if event.key == K_ESCAPE:
                # painettu ESCiä
                peli_kaynnissa = False

        elif event.type == QUIT:
            # ikkuna suljettu esim hiirellä
            peli_kaynnissa = False

    if paikka_muuttunut:
        print(f"paikkani on {x, y}")
        paikka_muuttunut = False

    pygame.display.flip()

pygame.quit()