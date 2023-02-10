a=int(input())
X=0
for i in range(a):
    b=input()
    if "++" in b:
        X+=1
    if "--"in b:
        X-=1
print(X)
