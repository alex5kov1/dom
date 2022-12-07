class InvalidParameterError(Exception):
    def __init__(self, name):
        self.name = name
        print(f"Invalid class parameter: {name}")

class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        self.age = age
        print(f"Invalid class parameter: {age}")

class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        self.sound = sound
        print(f"Invalid class parameter: {sound}")


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        if name != str:
            raise InvalidParameterError
        if age != int:
            raise InvalidAgeError
        if sound != str:
            raise InvalidSoundError

    def make_sound(self, name, sound):
        print(f"{name} says {sound}!")
    def print(self):
        pass
    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    super().__init__(self, name, age, sound)
    if age > 15
        raise InvalidAgeError
    if sound