a=input().split("+")
b=[]
for i in a:
    b.append(int(i))
d=sorted(b)
st=''
for i in d:
    st+=str(i)+"+"
print(st[:(len(st)-1)])
