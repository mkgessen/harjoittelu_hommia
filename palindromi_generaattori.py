""""
Tästä tehdään ohjelma joka luo palindromeja
"""

from palindromi.tunnistin import onko_palindromi
from palindromi.merkkijono import luo_merkkijonot

palindromit = []

for pituus in range(10):
    merkkijonot = luo_merkkijonot(pituus)
    for jono in merkkijonot:
        if onko_palindromi(jono):
            palindromit.append(jono)


for p in palindromit:
    print(p)



