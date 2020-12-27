for i in range(1,101):
    s=""
    if(i%5==0):
        s+="fizz"
    if(i%3==0):
        s+="buzz"
    if(len(s)<4):
        s=str(i)
    print(s)
