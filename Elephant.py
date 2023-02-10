a=int(input())
count=0
temp=a
while temp>0:
    if temp<5:
        count+=1
        temp=0
    elif temp==5:
        count+=1
        temp=0
    elif temp>5:
        count+=1
        temp-=5
print(count)
        
