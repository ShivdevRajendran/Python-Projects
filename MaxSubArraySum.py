from asyncio.windows_events import NULL
from json.encoder import INFINITY


def maxSubarraySum(arr, num):
    if (num > len(arr)):
        return NULL

    max = -INFINITY
    for i in range(0, len(arr) - num + 1):
        temp = 0
        for j in range(0, num):
            temp += arr[i + j]
        if (temp > max):
            max = temp
    return max

def maxSubarraySumEfficient(arr, num):
    maxSum = 0
    tempSum = 0
    if (len(arr) < num):
         return NULL

    for i in range(0, num):
        maxSum += arr[i]
    tempSum = maxSum
    for i in range(num, len(arr)):
        tempSum = tempSum - arr[i - num] + arr[i]
        if tempSum > maxSum:
            maxSum = tempSum
    return maxSum 

num = maxSubarraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3)
num2 = maxSubarraySumEfficient([2, 6, 9, 2, 1, 8, 5, 6, 3], 3)
print(num)
print(num2)