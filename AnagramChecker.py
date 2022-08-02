def anagramCheck(first, second):
    if ( len(first) != len(second) ):
        return False
    
    count1 = {}
    count2 = {}

    for i in range(0, 128):
        count1[i] = 0
        count2[i] = 0

    for i in range( 0, len(first) ):
        count1[ord(first[i])] += 1
        count2[ord(second[i])] += 1
    
    if count1 == count2:
        return True
    return False



string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
bool = anagramCheck(string1, string2)
print(bool)
