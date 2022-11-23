def sum_nums(a, b):
    return a+b

def sub_nums(a, b):
    return a-b

def dev_nums(a, b):
    return a/b

def multi_nums(a, b):
    return ab

print("Izberete operator: + - / ")

op_type = input()
a,b = eval(input("Vavedete dve chisla: "))

if op_type == "+":
    print(sum_nums(a,b))
elif op_type == "-":
    print(sub_nums(a,b))
elif op_type == "/":
    print(dev_nums(a,b))
elif op_type == "*":
    print(multi_nums(a,b))