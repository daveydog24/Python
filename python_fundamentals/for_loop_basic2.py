'''
For Loop Basic II
Created by: David Wukelic

    ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# Biggie Size - Given an array, write a function that changes all positive 
# numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns 
# that same array, changed to [-1, "big", "big", -5].

def makeItBig(arr):
    for index in range(0, len(arr) - 1):
        if arr[index] < 0:
            arr[index] = "big"
    
    return arr

print(makeItBig(array))

# Count Positives - Given an array of numbers, create a function to replace 
# last value with number of positive values. Example, countPositives([-1,1,1,1]) 
# changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered 
# to be a positive number).

def countPositives(arr):
    positives = 0

    for index in range(0, len(arr)):
        if arr[index] > 0:
            positives += 1
    
    arr[-1] = positives
    return arr

print(countPositives(array))

# SumTotal - Create a function that takes an array as an argument and returns 
# the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    total = 0

    for index in range(0, len(arr)):
        total += arr[index]
    
    return total

print(sumTotal(array))

# Average - Create a function that takes an array as an argument and returns 
# the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def multiples(arr):
    count = len(arr)
    total = 0

    for x in range(0, len(arr)):
        total += arr[0]

    avg = total / count
    return avg

print(multiples(array))

# Length - Create a function that takes an array as an argument and returns 
# the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    length = len(arr)
    return length

print(length(array))

# Minimum - Create a function that takes an array as an argument and returns 
# the minimum value in the array.  If the passed array is empty, have the 
# function return false.  For example minimum([1,2,3,4]) should 
# return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    min = 999999999999999 * 99999999999999

    for index in range(0, len(arr)):
        if arr[index] < min:
            min = arr[index]
    
    return min

print(minimum(array))

# Maximum - Create a function that takes an array as an argument and returns 
# the maximum value in the array.  If the passed array is empty, have the 
# function return false.  For example maximum([1,2,3,4]) should 
# return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    maximum = -9999999999999999

    for index in range(0, len(arr)):
        if arr[index] > maximum:
            maximum = arr[index]
    
    return maximum

print(maximum(array))

'''
array = [2, -4, 1, 33, -5, 9, -11, 22]

# UltimateAnalyze - Create a function that takes an array as an argument and 
# returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.






