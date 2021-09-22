class Ihminen:
    def __init__(self):
        self.nimi = "Otto"
        self.paikka_x = 123.123
        self.paikka_y= 321.321
    def liiku(self, x, y):
        self.place_x = x + self.paikka_x
        self.place_y = y + self.paikka_y
    def tulosta(self):
        print(f"Perttijuhanikallenpojan paikka on: {self.place_x, self.place_y}")
perttijuhanikallenpoika = Ihminen()

perttijuhanikallenpoika.nimi
perttijuhanikallenpoika.liiku(321.321, 123.123)
perttijuhanikallenpoika.tulosta()