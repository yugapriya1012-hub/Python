def remove_dup(st):
    a=[]
    for i in st:
        if i not in a:
            a.append(i)
    return a
print(remove_dup([1,2,3,1,4,5,2,3]))



