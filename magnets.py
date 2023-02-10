n=int(input())
b=[]
for i in range(n):
    j=input()
    b.append(j)
count=1
c=0
for i in range(1,len(b)):
    if b[c]!=b[i]:
        count+=1
    c+=1
    
        
print(count)        
        
    
