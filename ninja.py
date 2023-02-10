from pet import Pet
from dog import Dog
from cat import Cat
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

ninja_1 = Ninja("Alaa" , "Taieb", None, None, Dog(None))
ninja_2 = Ninja("Ahmed", "Derbali", None, None, Cat(None))

ninja_1.bathe()
ninja_2.bathe()