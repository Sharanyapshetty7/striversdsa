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

#or

n = int(input("enter: "))

spaces = 2*n - 2

for i in range(1, 2*n):
    stars = i

    if i > n:
        stars = 2*n - i

    for j in range(stars):
        print("*", end="")

    for j in range(spaces):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")

    print()

    if i < n:
        spaces -= 2
    else:
        spaces += 2
