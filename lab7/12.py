class InvalidParameterError(Exception):
    pass

class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food:
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fats = float(fats)
        self.salt = float(salt)
    def print_label(self):
        print(f"Food, ({self.carbs}, ({self.protein}), ({self.fats}), ({self.salt})")

for i in range(0, 120, 10):
    duner = Food(10.5, 65.7, 23, 102.1)
    try:
        if duner != float:
            raise InvalidParameterError
        if max(duner) > 100:
            raise NutrientError
        if sum(duner) == 0:
            raise InvalidFoodError
    except InvalidParameterError:
        print("Invalid parameter")
    except NutrientError:
        print("NutrientError")
    except InvalidFoodError:
        print("Invalid food")
    else:
        duner.print_label()