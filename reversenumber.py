n = int(input("enter: "))
copy = n
rev = 0

while(copy != 0):
    digit = copy % 10
    rev = rev * 10 + digit
    copy = copy // 10

print(f"the reverse of {n} is {rev}")
