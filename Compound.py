def compound(num, power):
    print(num)
    for x in range (0, power-1):
        num *= num
        print(num)
    return 

num = int(input("Enter a number: ") )
power = int(input("Enter the desired number of compounds: ") )
compound(num, power)


