def issorted(a):
    if len(a)==1 or len(a)==0:
        return True
    return a[0]<=a[1] and issorted(a[1:])
a=list(map(int,input().split()))
if issorted(a):
   print("This list is sorted")
else:
    print("This list is not sorted\nSorted list: ")
    b=sorted(a)
    print(*b)
