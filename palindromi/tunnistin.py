"""
Tämä on meidän hieno palindromin tunnistus moduuli
author: Otto ja Mathias
"""

def onko_palindromi(syote):
    """Tämän kommentin nimi on docstring

    Tämä funktio testaa onko annettu syöte palindromi
    :param syote: joku string joka halutan testata
    :return: palauttaa arvon True jos syöte oli palindromi. Muuten palauttaa Falsen.
    """
    return syote == syote[::-1]

