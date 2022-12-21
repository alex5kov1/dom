figure = input("Vavedte figure: ")

if figure == "kvadrat":
    from kvadrat import kvadratArea
    a = int(input("Vavedete a: " ))
    kvadratArea(a)

elif figure == "triugulnik":
    from triugulnik import triugulnikArea
    a = int(input("Vavedete a: " ))
    h = int(input("Vavedete h: "))
    triugulnikArea(a, h)

elif figure == "pravougulnik":
    from pravougulnik import pravougulnikArea
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    pravougulnikArea(a, b)

elif figure == "romb":
    from romb import rombArea
    a = int(input("Vavedete a: " ))
    ha = int(input("Vavedete ha: "))
    rombArea(a, ha)

elif figure == "trapec":
    from trapec import trapecArea
    a = int(input("Vavedete a: " ))
    b = int(input("Vavedete b: "))
    ha = int(input("Vavedete ha: "))
    trapecArea(a, ha, b)