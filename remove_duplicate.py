# def remove_dup(st):
#     a=[]
#     for i in st:
#         if i not in a:
#             a.append(i)
#     return a
# print(remove_dup([1,2,3,1,4,5,2,3]))

#find duplicate

def find_dup(a):
    dup=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                if a[i] not in dup:
                    dup.append(a[i])
    return dup
print(find_dup([1,2,1,2,4,5]))

