def factorial(num):
    total = 1
    for i in range(num, 1, -1):
        total *= i
        #print(total)
    return total

def factorialRecursion(num):
    if (num == 1): 
        return 1
    total = num * factorialRecursion(num - 1)
    return total

num = int(input("Enter a number to add up to: ") )
print(factorial(num))
print(factorialRecursion(num))