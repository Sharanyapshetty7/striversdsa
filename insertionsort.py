n=int(input("enter the size of the array: "))
a=[]
for i in range(n):
  ele=int(input(f"enter the {i}th element: "))
  a.append(ele)


for i in range(n):
  j=i
  while j>0 and a[j-1]>a[j]:
    temp=a[j]
    a[j]=a[j-1]
    a[j-1]=temp
    j-=1

print(f"the sorted array is: {a} ")
