arr=[1,2,3,4,5,6,7]


temp=[]
d=3
n=len(arr)
d=d%n
for i in range(d):
  temp.append(arr[i])

for i in range(d,n):
  arr[i-d]=arr[i]

for i in range(n-d,n):
  arr[i]=temp[i-(n-d)]

  
print(arr)
