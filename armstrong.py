n = int(input("Enter a number: "))

copy = n
sum = 0
count = 0

# Count the number of digits
while copy != 0:
    copy = copy // 10
    count += 1

# Find the sum of powers of digits
copy = n

while copy != 0:
    digit = copy % 10
    sum = sum + (digit ** count)
    copy = copy // 10

# Check Armstrong
if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
