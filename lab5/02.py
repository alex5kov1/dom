def isPalindrome(string):
    if (string == string[::-1]) :
        return "True"
    else:
        return "False"

string = input("Vavedete chislo: ")

print(isPalindrome(string))