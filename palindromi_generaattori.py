""""
Tästä tehdään ohjelma joka luo palindromeja
"""


import itertools
from palindromi.tunnistin import onko_palindromi
from palindromi.merkkijono import luo_merkkijonot, AAKKOSET

palindromit = []

for r in range(4, 6):https://www.amazon.co.uk/Wacom-Cintiq-Creative-Display-DTK-2260/dp/B07TR7YQ8Y
    print(f'lasketaan kaikki {r} merkkiä pitkät merkkijonot', end=" ")
    for s in itertools.product(AAKKOSET, repeat=r):
        mjono = ''.join(s)
        #print(".", end=" ")
        if onko_palindromi(mjono):
            palindromit.append(mjono)
            #print(f"löytyi palindromi {mjono}")
    print('')


print(f"löytyi {len(palindromit)} palindromia")



