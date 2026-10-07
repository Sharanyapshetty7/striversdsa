#moving zeros to the end
nums=[1,0,2,3,2,0,0,4,5,1]
n=len(nums)
temp=[]
for i in range(len(nums)):
  if nums[i]!=0:
    temp.append(nums[i])


for i in range(len(temp)):
  nums[i]=temp[i]

nt=len(temp)
n
for i in range(nt,n):
  nums[i]=0



print(nums)
  
