a=int(input())
for i in range(a):
    b=input()
    c=int(b)
    s=0
    for i in b:
        s+=int(i)
        w=1
        x=[1]
        while w==1:
            for i in range(1,c):
                if c%i==0 and s%i==0 and s>i+1:
                    x.append(i)
                    print(x)
                gcd=x[-1]
            if gcd!=1:
                print(gcd)
                w=gcd
            else:
                x=[]
                s+=1
                c+=1
    
                    
                
