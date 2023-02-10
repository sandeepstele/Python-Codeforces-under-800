n=int(input())
b="I hate"
c="I love"
c="I love that "
d=""
e="I hate that "

if n==1:
        print(b+" it")
        
else:
    i=1
    d=e
    while i!=n:
        if i%2!=0:
            d+=c
            i+=1
        elif i%2==0:
            d+=e
            i+=1
        
    print(d[:-5]+"it")
        
