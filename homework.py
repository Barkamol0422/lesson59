def length(a):
    if a==[]:
        return 0
    else:
        return 1+length(a[1:])
a=[1,1,1,1,1,1,2]
print(length(a))
