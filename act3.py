def sumofa(a):
    if len(a)==1:
        return a[0]
    return a[0]+sum(a[1:])
a=list(map(int,input().split()))
print(sumofa(a))
