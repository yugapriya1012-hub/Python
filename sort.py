def sort(a):
    l=len(a)
    for i in range(l):
        for j in range(0,l-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
sort([7,1,5,4,3])