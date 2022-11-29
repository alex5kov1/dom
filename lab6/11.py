class Vehicle:
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers})")

class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, price, kosh):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers=2)
        self.price = price
        self.kosh = kosh

    def print_info(self):
        print(
            f"Vehicle({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.price}, {self.kosh})")

class Car(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, category, fuel_type):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers=4)
        self.category = category
        self.fuel_type = fuel_type

    def print_info(self):
        print(
            f"Vehicle({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.category}, {self.fuel_type})")

class Bus(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, company, year):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.company = company
        self.year = year

    def print_info(self):
        print(
            f"Vehicle({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.company}, {self.year})")


list = []
s1 = Car("Opel", "Astra H", 1.6, 190.0, 200000.0, 4, "hatcback", "gasoline")
s2 = Motorbike("Yamaha", "T-max", 1.0, 240.0, 29000.0, 2, 65000.2, False)
s3 = Bus("Mercedes", "Tourier", 3.5, 120.0, 115000.1, 63, "Cratos", 2020)
s4 = Car("Audi", "S4 b8", 3.0, 250.0, 150000.0, 4, "estate", "gasoline")
s5 = Motorbike("KTM", "Duke", 1.2, 190.0, 20000.0, 2, 32000.2, False)
s6 = Bus("Iveco", "Evadys", 4.8, 130.0, 130000.5, 60, "Nirabus", 2022)
s7 = Car("Ford", "Mondeo mk5", 1.5, 200.0, 210000.0, 4, "hatcback", "gasoline")
s8 = Motorbike("Kawasaki", "Ninja", 1.0, 300.0, 31000.3, 2, 50000.2, False)
s9 = Bus("MAN", "Lion", 4.0, 100.0, 100000.0, 50, "Union Uvkani", 2023)
s10 = Car("BMW", "E90", 2.0, 220.0, 180000.0, 4, "estate", "diesel")

list.append(s1)
list.append(s2)
list.append(s3)
list.append(s4)
list.append(s5)
list.append(s6)
list.append(s7)
list.append(s8)
list.append(s9)
list.append(s10)

s1.print_info()
s2.print_info()
s3.print_info()
s4.print_info()
s5.print_info()
s6.print_info()
s7.print_info()
s8.print_info()
s9.print_info()
s10.print_info()

print(list)
