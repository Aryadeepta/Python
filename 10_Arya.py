import random
x=int(1/(random.random()*random.random()*random.random()*random.random()*random.random()*random.random()*random.random()*random.random()))
i=-1
while(i!=x):
    i=int(input("Guess: "))
    if i>x:
        print("Lower")
    elif i<x:
        print("Higher")
    else:
        print("Correct")
