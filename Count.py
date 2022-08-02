def countUp(n):
    print("Counting Up...")
    for x in range(0, n+1):
        print(x)


def countDown(n):
    print("Counting Down...")
    for x in range(n, -1, -1):
        print(x)

num = int(input("Enter a number: "))
countUp(num)
countDown(num)