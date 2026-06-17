def str_count(word):

    u=0
    l=0
    for i in word:
        if i.isupper():
            u=u+1
        else:
            l=l+1
    print("Upper:", u, "Lower:", l)
str_count("Hello Everyone!")