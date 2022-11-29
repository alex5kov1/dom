class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"{self.name}, {self.family}, {self.age}, {self.nationality}")


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(f"{self.name}, {self.family}, {self.age}, {self.nationality}, {self.university}, {self.year_of_study}")

list = []
A = Student("Alex", "Petkov", "19", "bulgarian", "TU", "First")
H = Student("Hristo", "Evtimov", "19", "bulgarian", "TU", "First")
I = Student("Ivan", "Vasilev", "19", "Bulgarian", "TU", "First")

list.append(A)
list.append(H)
list.append(I)

A.print()
H.print()
I.print()