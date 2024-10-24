class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издаёт звук")

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wind_span} м")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")

    def run(self):
        print(f"{self.name} бежит")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит")

    def crawl(self):
        print(f"{self.name} ползет")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

parrot = Bird(name="Попугай", age=3, wing_span=0.5)
tiger = Mammal(name="Тигр", age=5, fur_color="Оранжевый")
snake = Reptile(name="Змея", age=2, scale_type="Гладкая")

animals = [parrot, tiger, snake]

animal_sound(animals)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name} ")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name} ")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"В зоопарк добавлено животное: {animal.name} ")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"В зоопарк принят сотрудник: {staff_member.name}")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f" - {animal.name} ")

    def show_staff(self):
        print(f"Сотрудники зоопарка {self.name}:")
        for member in self.staff:
            print(f" - {member.name}")

zookeeper = ZooKeeper("Анна")
vet = Veterinarian("Доктор Иван")

zoo = Zoo(name = "Зоопарк Мечта")

zoo.add_animal(tiger)
zoo.add_animal(parrot)
zoo.add_staff(zookeeper)
zoo.add_staff(vet)