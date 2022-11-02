num = int(input("Enter number:"))
bit = int(input("Enter bit:"))
if num & (1 << bit) > 0:
    print("False")
else:
    print("True")