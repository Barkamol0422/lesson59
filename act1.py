def issorted(a):
    length=len(a)
    if length==1 or length==0:
        return True
    return a[0]<=a[1] and issorted(a[1:])
a=[1,2,3,4,5,6,7,8]
if issorted(a):
    print("Sorted")
else:
    print("Not sorted")
