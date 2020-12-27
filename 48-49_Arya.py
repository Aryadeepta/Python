import numpy as np
def inputMatrix():
    r=int(input("rows: "))
    c=int(input("columns: "))
    return(np.array([[int(j) for j in input().split()][:c] for i in range(r)]))
flag=True
while flag:
    path=input("Would you like to\n1: Determinant of matrix\n2: Multiply matrices\nAnything else: quit\n")
    if(path=='1'):
        print(int(np.linalg.det(inputMatrix())))
    elif(path=='2'):
        print(np.matmul(inputMatrix(), inputMatrix()))
    else:
        flag=False
