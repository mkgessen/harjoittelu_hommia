""""
Tästä tehdään ohjelma joka luo palindromeja
"""

import itertools
from palindromi.tunnistin import onko_palindromi
from palindromi.merkkijono import luo_merkkijonot, AAKKOSET

palindromit = []


for r in range(4, 10):
    print(f'lasketaan kaikki {r} merkkiä pitkät merkkijonot', end=" ")
    for s in itertools.product(AAKKOSET, repeat=r):
        mjono = ''.join(s)
        #print(".", end=" ")
        if onko_palindromi(mjono):
            palindromit.append(mjono)
            #print(f"löytyi palindromi {mjono}")
    print('')


for p in palindromit:
    print(p)



