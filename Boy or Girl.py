a=input()
b=[]
c=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j] and i!=j :
            if a[i] not in c:
                c.append(a[i])
            break
    else:
        b.append(a[i])
b+=c
if len(b)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
            
    
