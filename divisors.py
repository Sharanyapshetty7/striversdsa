n = int(input("Enter the number: "))
if n<=0:
    print("no factors please enter number above 0")
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)


print(f"factors of {n} are {factors}")
