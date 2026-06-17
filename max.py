def max(a):
    max=a[0]
    for i in range(1,len(a)):
        if a[i]>max:
            max=a[i]
    return max
print(max([1,2,3,4,5]))


#second max

def second_max(n):
    first=n[0]
    second=n[0]
    for i in range(len(n)):
        if n[i]>first:
            second=first
            first=n[i]
        elif n[i]>second and n[i]!=first:
            second=n[i]
    return second
print(second_max([1,2,3,4,5]))