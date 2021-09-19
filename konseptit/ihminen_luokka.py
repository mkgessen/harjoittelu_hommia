
class Ihminen:
    def __init__(self):
        self.nimi = ""
        self.paikka_x = 0.0
        self.paikka_y = 0.0
        self.kaveri = None

    def liiku(self, x_maara, y_maara):
        self.paikka_x = self.paikka_x + x_maara
        self.paikka_y = self.paikka_y + y_maara

    def tulosta(self):
        print(f"Ihminen nimeltä {self.nimi}")
        print(f"paikka {self.paikka_x}, {self.paikka_y}")

otto = Ihminen()
otto.nimi = "Otto"
otto.liiku(100.0, 20.0)
otto.tulosta()

mathias = Ihminen()
mathias.nimi = "Mathias"
mathias.liiku(10.0, -20.7)
mathias.tulosta()

otto.kaveri = mathias
otto.kaveri.liiku(1000.0, 0)
otto.kaveri.tulosta()


