n=int(input())
for i in range(n):
    a=input()
    b=input()
    count=0
    for i in a:
        if i==b:
            count+=1
    if len(a)==1:
        print("NO")
    elif count==1:
        for i in range(len(a)):
            if a[i]==b and i%2==0:
                print("YES")
                break
        else:
            print("NO")
    elif count>1:
        for i in range(0,len(a),2):
            if a[i]==b:
                print("YES")
                break
        else:
                print("NO")
            
    
