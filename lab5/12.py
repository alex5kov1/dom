#не работи
list = [5, 7, 2]

def list_avg(lst):
    result = 0
    for i in lst:
        if type(i)==int:
            average = sum(lst)/len(lst)
    return lst

print(list_avg(list))
