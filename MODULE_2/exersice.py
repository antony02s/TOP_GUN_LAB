class Animal:
    def make_noise(self, name):
        print(f"I am a {name} and I will make noise")


class Dog(Animal):
    def make_noise(self):
        super().make_noise("Dog")
        print("woof woof")

class Human(Animal):
    def make_noise(self):
        super().make_noise("Human")
        print("I am a programmer")


dog = Dog()
human = Human()


dog.make_noise()
human.make_noise()


class SuperInteger(int):
    # solucionar el problaema usando metodo new
    def __init__(self, value) -> None:
        super().__init__(value)


special_number = SuperInteger(21)
print(special_number.info)
