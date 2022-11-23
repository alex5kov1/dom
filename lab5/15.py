def can_triangle_exist(a, b, c):
    if n_1 + n_2 >= n_3 and n_1 + n_3 >= n_2 and n_2 + n_3 >= n_1:
        return 'True'
    else:
        return 'False'

n_1 = int(input("A: "))
n_2 = int(input("B: "))
n_3 = int(input("C: "))
is_valid_triangle = can_triangle_exist(n_1, n_2, n_3)
print(is_valid_triangle)