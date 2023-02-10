a=input().split()
d=a[0]
e=a[1]
b=int(d)
c=int(e)
t=c
while t!=0:
    if (b)%10!=0:
        (b)-=1
    else:
        b=b//10
    t-=1
print(b)
