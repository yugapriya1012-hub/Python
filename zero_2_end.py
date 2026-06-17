def zero_to_end(n):
    a=[]
    b=[]
    for i in range(0,len(n),1):
        if n[i]>0:
            a.append(n[i])
        else:
            b.append(n[i])
    print(a+b)
zero_to_end([1,3,4,0,5,4,0,8,9])