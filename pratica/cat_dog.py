class Animal:
    def fazer_som(self):
        pass


class Cachorro():
    def fazer_som(self):
        return "Au Au!"


class Gato():
    def fazer_som(self):
        return "Miau!"


class Vaca():
    def fazer_som(self):
        return "Moo!"


cachorro = Cachorro()
gato = Gato()
vaca = Vaca()
print(cachorro.fazer_som())
print(gato.fazer_som())
print(vaca.fazer_som())

