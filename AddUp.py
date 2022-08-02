def addUpTo(n):
    total = 0
    for x in range(0, n + 1, 1):
        total += x
    return total

def addUpEfficient(n):
    ans = (n * (n+1) ) / 2
    return ans

def sumRange(n):
    if (n == 1): return 1
    return n + sumRange(n-1)

num = int(input("Enter a number to add up to: ") )
print(addUpTo(num))
print(addUpEfficient(num))
print(sumRange(num))



