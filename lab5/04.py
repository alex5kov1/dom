def num_list(lst, num):
    for i in lst:
        if type(i)==int:
            if i>num:
                lst[lst.index(i)]=0
    return lst

print(num_list([4, 6, 'f', 2, 5, 9], 3))
