def isArmstrong(num):
    d=len(str(num))
    n1=num
    n2=0
    while n1>0:
        n2+=(n1%10)**d
        n1//=10
    return num==n2
print(isArmstrong(154))