num_count = int(input('Vuvedete broia na chislata: '))
max_num = 0
i = 1
while i <= num_count:
    num = int(input(f'Vuvedete chislo {i}: '))
    if num > max_num:
        max_num = num

    i += 1
print(f"Nai golqmoto chislo e {max_num}")