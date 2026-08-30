n=int(input("enter: "))
s=chr(65)
for i in range(1,n+1):
    for j in range(i):
        print(s,end=" ")
    s=chr(65+i)
    print()
