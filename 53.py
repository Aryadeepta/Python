##Write a program that determines whether a 3x3 grid is a valid sudoku solution
##(each column and row contains the numbers 1-3 exactly once). Bonus 50 points:
##how many valid configurations are there?
## there are 12 valid configurations
x=[[int(j) for j in input().split()] for i in range(3)]
f=True
for i in range(3):
    a=1
    b=1
    for j in range(3):
        a*=x[i][j]
        b*=x[j][i]
    if(a!=6 or b!=6):
        f=False
        break
print(f)
