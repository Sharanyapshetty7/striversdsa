

def reverses(arr,start,end):
  while start<=end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    start+=1
    end-=1

def rotate(nums,d):
  n=len(nums)
  d=d%n
  reverses(nums,0,d-1)
  reverses(nums,d,n-1)
  reverses(nums,0,n-1)


arrr=[1,2,3,4,5,6,7]

rotate(arrr,3)
print(arrr)
