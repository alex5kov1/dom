num = int(input("Enter number:"))
bit = int(input("Enter bit:"))
if num & (1 << bit) > 0:
    print("True")
else:
    print("False")