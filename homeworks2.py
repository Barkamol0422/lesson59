def powerof2(number):
    if number==0:
        return False
    if number==1:
        return True
    if number%2==0:
        return powerof2(number/2)
        
    return False
n=int(input("Enter a number: "))
print(powerof2(n))
