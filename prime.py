def prime(n):
    if n%2==0:
        return "It's a prime"
    if n<2:
        return "Not a prime"
    for i in range(2,n):
        if n%i==0:
            return "Not a prime"
    return "Prime"
print(prime(9))
    