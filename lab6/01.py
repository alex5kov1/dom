class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"{self.name}, {self.family}, {self.age}, {self.nationality}")

list = []
A = Person("Alex", "Petkov", "19", "bulgarian")
H = Person("Hristo", "Evtimov", "19", "bulgarian")
I = Person("Ivan", "Vasilev", "19", "Bulgarian")

list.append(A)
list.append(H)
list.append(I)

A.print()
H.print()
I.print()