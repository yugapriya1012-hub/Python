def char_count(a):
    count={}
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
print(char_count("hello"))


def count(num):
    count={}
    for i in num:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return count
print(count([1,2,1,3,2,1]))