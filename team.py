a=int(input())
count=0
temp=0
for i in range(a):
    a=input().split()

    for i in a:
        if i=="1":
            temp+=1
            
    if temp>=2:
        count+=1
    temp=0
print(count)
    
 
