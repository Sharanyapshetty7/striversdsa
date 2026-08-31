n = int(input("enter: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")

    ch = "A"
    breakpoint = (2*i+1) // 2

    for j in range(2*i+1):
        print(ch, end="")

        if j < breakpoint:
            ch = chr(ord(ch) + 1)
        else:
            ch = chr(ord(ch) - 1)
#ord()=converts character to unicode and similiarly chr()=converts character to unicode 

    for j in range(n-i-1):
        print(" ", end="")

    print()
