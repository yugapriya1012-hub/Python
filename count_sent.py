def count_sent(sent):
    count={}
    str=''
    list=[]
    for i in sent:
        if i!=" ":
            str=str+i
        else:
            list.append(str)
            str=''
    list.append(str)
    for i in list:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    print(count)
count_sent("python is a good and python is easy")
