n = int(input("Enter the number: "))

# FIX: Check for negative numbers immediately to prevent infinite loops
if n < 0:
    print("Armstrong numbers are only defined for positive integers.")
else:
    copy = n
    copy2 = n
    count = 0
    arm = 0

    # Count the number of digits
    if n == 0:
        count = 1
    else:
        while copy != 0:
            count += 1
            copy = copy // 10

    print(f"The number of digits are {count}")

    # Calculate the Armstrong sum
    while copy2 != 0:
        dig = copy2 % 10
        arm = arm + (dig ** count)
        copy2 = copy2 // 10

    # Check if it is an Armstrong number
    if arm == n:
        print("The number is an Armstrong number")
    else:
        print("The number is not an Armstrong number")

