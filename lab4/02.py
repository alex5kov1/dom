number = int(input("Vavedete chislo:"))
result = 1

for i in range(1, number + 1):
    result = i * result

print(result)