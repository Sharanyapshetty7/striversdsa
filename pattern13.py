num=1
n=int(input("enter: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
