def count(string):
    display = {}
    chars = {}
    nums = {} 
    for i in range(0, 128):
        chars[i] = chr(i)
        nums[i] = 0
    
    display = {chars[i]: nums[i] for i in range(len(chars))}

    for j in range(0, len(string)):
        display[string[j]] += 1

    for i in display:
        if (display[i] > 0):
            print(i + " - " + str(display[i]))





string = input("Enter any string: ")
count(string)