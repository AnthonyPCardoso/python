class Animal:

    def __init__(self, nome):

        self.nome = nome



    def mover(self):

        print("Animal se movendo...")



class Terrestre(Animal):

    def mover(self):

        print("Animal terrestre se movendo...")



class Aquatico(Animal):

    def mover(self):

        print("Animal aquático se movendo...")



class Voador(Animal):

    def mover(self):

        print("Animal voador se movendo...")



def fazer_animal_mover(animal):

    animal.mover()



animais = [Terrestre("Leão"), Aquatico("Peixe"), Voador("Águia")]



for animal in animais:

    fazer_animal_mover(animal)

