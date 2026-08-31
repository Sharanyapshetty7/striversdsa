n=int(input("enter: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(2*n-(2*i)):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    for j in range(n*2-(2*i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()
