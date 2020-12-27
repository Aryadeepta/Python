import random
def inCircle(c,r,p):
    return((c[0]-p[0])**2+(c[1]-p[1])**2<r**2)
flag=True
while flag:
    path=input("Would you like to:\n1: see if a point is in a circle\n2: Approximate pi/4 with points in a square\nAnything else: Quit\n")
    if(path=='1'):
        print(inCircle((int(input("Center X: ")),int(input("Center Y: "))),int(input("Radius: ")),(int(input("Point X: ")),int(input("Point Y: ")))))
    elif(path=='2'):
        print(sum([int(inCircle((.5,.5),.5,(random.random(),random.random()))) for i in range(10000)])/10000)
    else:
        flag=False
