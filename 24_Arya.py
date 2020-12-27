x=int(input("Power of e: "))
f=1
i=1
j=0
s=0
while(i/f>=s*.0001):
    s+=i/f
    j+=1
    f*=j
    i*=x
print("Approximation of e^"+str(x)+" with .1% error (with "+str(j)+" terms): "+str(s))
