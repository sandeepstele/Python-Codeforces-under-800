a=[0,0]
e=[]
b=int(input())
for i in range(1):
    c=int(input())
    d=input()
    for i in range(len(d)):
        
            if d[i]=="U":
                a[0]+=1
                print(a)
                e.append(a)
                print(e)
                
            elif d[i]=="D":
                a[0]-=1
                print(a)
                e.append(a)
                print(e)
                
            elif d[i]=="R":
                a[1]+=1
                print(a)
                e.append(a)
                print(e)

            elif d[i]=="L":
                a[1]-=1
                print(a)
                e.append(a)
                print(e)
            else:
                print(e)

            
            
            
    
