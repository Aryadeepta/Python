(a,b)=(int(i) for i in input().split())
(x,y)=(a,b)
g=0
## Euclid:
while g==0:
    if(b>a):
        c=a
        a=b
        b=c
    elif(a*b==0):
        g=(a+b)
    else:
        a%=b
print("GCF: "+str(g))
## LCM
print("LCM: "+str(int(x*y/g)))
