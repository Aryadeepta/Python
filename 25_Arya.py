x=int(input("Number: "))
i=2
while i**2<=x:
    if(x%i==0):
        print(i)
        x=int(x/i)
    else:
        i+=1
if(x!=1):
    print(x)
