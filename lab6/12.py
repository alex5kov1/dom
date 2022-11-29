class Animal:
    def __init__(self, name, age, type_food):
        self.name = name
        self.age = age
        self.type_food = type_food

    def make_sound(self):
        pass

    def eat_food(self, quantity):
        pass


class Cat(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, quantity):
        if quantity == 0:
            for x in range(4):
                self.make_sound()
            return 0
        elif quantity < 10:
            for x in range(2):
                self.make_sound()
            return 0
        return quantity - 10


class Dog(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Djaf-djaf!")

    def eat_food(self, quantity, eat_quantity=5):
        result = quantity - eat_quantity
        if result >= 0:
            return result
        return 0


class Duck(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Quack-Quack!")

    def eat_food(self, quantity):
        self.make_sound()
        import random
        random_number = random.randint(1, 9)
        if random_number > quantity:
            return 0
        return quantity - random_number


class Horse(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("IIUUHHHH!")

    def eat_food(self, quantity):
        if quantity > 30:
            result = quantity - 15
        else:
            result = quantity - 8
        if result < 0:
            return 0
        return result



dic_food = {"meat":200, "fish":200, "grass": 90, "apples": 300}

a1 = Cat("Gecata", 6, "fish")
a2 = Cat("Katie", 4, "fish")
a3 = Duck("Naco", 2, "grass")
a4 = Horse("Lucho", 8, "apples")
a5 = Dog("Kira", 3, "meat")
a6 = Duck("Sevtopolis", 7, "grass")
a7 = Cat("Tom", 9, "fish")
a8 = Duck("Donald", 1, "grass")
a9 = Dog("Betoven", 4, "meat")
a10 = Horse("Vihar", 10, "apples")

list_animals = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]


for x in list_animals:
    print("-------------------")
    for i in range(10):

        class_name = list_animals[i].__class__.__name__
        name_animal = list_animals[i].name
        food = list_animals[i].type_food
        left_food = list_animals[i].eat_food(dic_food[food])
        print(f"{name_animal} the {class_name} just ate {dic_food[food]-left_food} {food}, "
              f"there's {left_food} left")
        dic_food[food] = left_food