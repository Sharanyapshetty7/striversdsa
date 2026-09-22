n=int(input("enter the size of the array: "))
nums=[]
for i in range(n):
  ele=int(input(f"enter the {i}th element: "))
  nums.append(ele)


for i in range(n-1,0,-1):
  didswap=0
  for j in range(0,i):
    if nums[j]>nums[j+1]:
      nums[j],nums[j+1]=nums[j+1],nums[j]
      didswap+=1
  if(didswap==0):
    break

print(f"the sorted array is: {nums} ")
