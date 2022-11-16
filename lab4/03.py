number = int(input("Vuvedete chislo:"))
list_1 = []

for i in range(0, number):
    number_2 = int(input("Vavedete drugo chislo:"))
    list_1.append(number_2)

for i in range(0, number):
    number_3 = int(input("Vavedete 0 ili 1:"))
    if number_3 == 0:
        if i % 2 == 0:
            list_1[i] = list_1[i] + 5
    elif number_3 == 1:
        if i % 2 != 0:
            list_1[i] = list_1[i] + 10
    else:
        print("Greshka:")

print(list_1)
