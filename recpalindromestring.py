def palindrome(i):
  if i>=n//2:
    return True
  if a[i]!=a[n-i-1]:
    return False
  return palindrome(i+1)



a=input("enter the string ")
n=len(a)

print(palindrome(0))
