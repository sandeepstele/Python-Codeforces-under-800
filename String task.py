a=input()
b=['a','e','i','o','u','y','A','E','I','O','U','Y']
st=''
strr=''
c=[]
d=[]
for i in a:
    c.append(i)

try:
    for i in range(len(c)):
        if c[i] not in b:
            d.append(c[i])
            
except IndexError:
    pass
for i in d:
    st+=i
for i in st:
    strr+='.'+i.lower()
print(strr)
        
         
