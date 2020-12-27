def dist(a,b):
    return((sum([(a[i]-b[i])**2 for i in range(len(a))]))**.5)
a=(int(input("Ax: ")),int(input("Ay: ")),int(input("Az: ")))
b=(int(input("Bx: ")),int(input("By: ")),int(input("Bz: ")))
c=(int(input("Cx: ")),int(input("Cy: ")),int(input("Cz: ")))
(A,B,C)=(dist(b,c),dist(c,a),dist(a,b))
S=(A+B+C)/2
print((S*(S-A)*(S-B)*(S-C))**.5)
