"""
Tästä tehdään ohjelma joka tunnistaan onko merkkijono palindromi vai ei

"Palindromi on sana, virke, luku tai mikä tahansa merkkijono, jonka merkkien järjestys on etu- ja takaperin sama."
(Wikipedia)

Miten tietokone voisi tunnistaa palindromin?


"""

syote = input("syötä palindromi: ")
foo = 0

#  4 merkin erikoistapaus/esimerkki josta lähdettiin liikellee
# if syote[0] == syote[3] and syote[1] == syote[2]:
#     print("Se on palindromi!!!")
# else:
#     print("Eihän ole")
#

kaannetty_syote = syote[::-1]
if syote == kaannetty_syote:
    print("On palindromi")
else:
    print("Eihän ole")

"""
Tämä on ihan kamala tapa testata onko palindromi, mutta voi auttaa silmukoiden ja 
if-lauseiden opettelua

syote = "OTTO"
pituus = len(syote) --> pituus = 4 

---------------------------------
|   0   |   1   |   2   |   3   |
---------------------------------
|   O   |   T   |   T   |   O   | 
---------------------------------
"""

# pituus = len(syote)
# on_palindromi = True
# for indeksi in range(int(len(syote) / 2)):
#
#     # Indeksi = 0:  syote[0]->O    pituus-indeksi-1 = 4-0-1 = 3, syote[3]->O
#     #           1:  syote[1]->T    pituus-indeksi-1 = 4-1-1 = 2, syote[2]->T
#     if syote[indeksi] == syote[pituus-indeksi-1]:
#         print(f"Testaan '{syote[indeksi]}' vs '{syote[pituus-indeksi-1]}': Voi olla palindromi")
#     else:
#         on_palindromi = False
#         break
#
# if on_palindromi:
#     print(f"{syote} on palindromi")
# else:
#     print(f"{syote} ei ollut palindromi")
