a=int(input())
b=input().split()
c=sorted(b,reverse=True)
d=[]
sum11=0
sum1=0
x=0
for i in c:
    d.append(int(i))
for i in range(len(d)):
    sum1+=d[i]
    sum11=sum(d[i+1:])
    if sum1>sum11:
        print(i+1)
        break
    
