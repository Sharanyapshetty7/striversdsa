n = 5

for i in range(n, 0, -1):
    # spaces
    for j in range(n - i):
        print(" ", end="")

    # stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()