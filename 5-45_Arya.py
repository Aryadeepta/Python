import random
## 5
x=0
while x<1:
    x+=random.random()
print(x)
## 45
t=0
for zebra in range(10000):
    x=0
    c=0
    while x<1:
        x+=random.random()
        c+=1
    t+=c
print("The average number of tries is "+str(t/10000)+", which is close to e")
