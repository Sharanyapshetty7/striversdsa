def reversearray(i):
  if i>=n//2:
    return
  a[i],a[n-i-1]=a[n-i-1],a[i]
  reversearray(i+1)


n=int(input("enter "))
a=[]
for i in range(n):
  ele= int(input(f"enter the {i}th element "))
  a.append(ele)
reversearray(0)
print(a)
