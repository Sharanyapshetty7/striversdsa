n=int(input("enter the size of the array: "))
arr=[]
for i in range(n):
  ele=int(input("enter the element: "))
  arr.append(ele)

#precompute
hash=[0]*13
for i in range(n):
  hash[arr[i]]+=1

queryno=int(input("enter total number of query: "))
while queryno>0:
  num=int(input("enter: "))
  #fetch
  print(hash[num])
  queryno -= 1
