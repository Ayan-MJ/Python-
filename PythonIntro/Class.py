class ToyCar:
    def __init__(self, color):
        self.color = color

    def drive(self):
        print(f"{self.color} is the one you are driving")

car1 = ToyCar("Blue")
car2 = ToyCar("Red")

car1.drive()
car2.drive()

class pet:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

    def speak(self):
        print(f"say hello {self.name}")

    def do_trick(self, trick):
        print(f"{self.name} do a {trick}!")


pet1 = pet("Buddy", "dog")
pet2 = pet("Whisker", "cat")
pet3 = pet("Charlie", "Parrot")

print(pet1.name)
print(pet2.species)

pet1.speak()
pet2.speak()
pet3.speak()