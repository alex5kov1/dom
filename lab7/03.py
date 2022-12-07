import math

try:
    n = int(input("Vavedete chislo: "))
    if n > 0:
        print(math.sqrt(n))
    else:
        raise ValueError
except (ValueError):
        print("Invalid number")
finally:
    print("Good Bye")