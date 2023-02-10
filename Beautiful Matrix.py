a,b,c,d,e= input().split(),input().split(),input().split(),input().split(),input().split()
for i in range(5):
    if a[i]=="1":
        x="1x"+str(i+1)
for i in range(5):
    if b[i]=="1":
        x="2x"+str(i+1)

for i in range(5):
    if c[i]=="1":
        x="3x"+str(i+1)
for i in range(5):
    if d[i]=="1":
        x="4x"+str(i+1)
for i in range(5):
    if e[i]=="1":
        x="5x"+str(i+1)
y=x.split('x')
print(abs(3-int(y[0])+abs(3-int(y[1]))))
