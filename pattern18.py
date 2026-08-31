n = int(input("enter: "))
ch='E'
chh='E'


for i in range(1,n+1):
    for j in range(1,i+1):
        
        if i==j:
            print(chh,end="")
        else:
            ch=chr(ord(chh)-(i-j))
            print(ch,end="")


            

    print()    
