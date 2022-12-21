operacia = input("Vavedete operacia: ")

if operacia == "umnojenie":
    from umn import umnojenie
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    umnojenie(a, b)

if operacia == "delenie":
    from dele import delenie
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    delenie(a, b)

if operacia == "subirane":
    from sub import subirane
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    subirane(a, b)

if operacia == "izvajdane":
    from izv import izvajdane
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    izvajdane(a, b)