a = int(input("enter: "))
b = int(input("enter: "))

gcdd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcdd = i

print(gcdd)
