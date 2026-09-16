n=input("enter the string: ")
stringlen=len(n)

#precompute
hash=[0]*27
for i in range(stringlen):
  hash[ord(n[i])-ord('a')]+=1

queryno=int(input("enter total number of query: "))
while queryno>0:
  chara=input("enter: ")
  #fetch
  print(hash[ord(chara)-ord('a')])
  queryno -= 1
