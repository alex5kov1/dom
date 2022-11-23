def kvadrat(a):
    return a**2

def pravougulnik(a, b):
    return a*b

def triugulnik(a, b):
    return a*b/2

print("Izberete kvadrat, pravougulnik ili triugulnik")

op_type = input()
a,b = eval(input("Vavedete chislata: "))

if op_type == "kvadrat":
    print(kvadrat(a))
elif op_type == "pravougulnik":
    print(pravougulnik(a,b))
elif op_type == "triugulnik":
    print(triugulnik(a,b))
















