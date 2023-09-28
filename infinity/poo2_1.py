class Animal:

    def __init__(self, name):

        self.name = name

    def speak(self):

        return "O animal faz barulho."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "O cachorro late."


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):

        return "O gato mia."

dog = Dog("Rex", "Labrador")

print(dog.name)