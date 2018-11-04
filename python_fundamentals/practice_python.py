# This is a file to test python functions and techniques.


# y = ["The boy went to the zoo", 5, 33, 12, "friends", 56, "winning", "testing", 11]
# string = ""
# total_sum = 0

# for x in y:
#     if isinstance(x, str):
#         string += x + " "
#     elif isinstance(x, int):
#         total_sum += x
        
# print(string)
# print(total_sum)

# inclusive left
# exclusive right
# in left
# ex right
# in:ex
# in and out
# [in:out]
# [1:5]
#  ->>>>>> will print anything from index 1 up to index 5 

def square(num):
    return num * num

def double(num):
    return num + num
    
arr = [-121122, 1,2,3,4,5, 9999999999]
# includes all numbers in the list besides the first and last index 
# or the min and max in a sorted array
x = arr[1:(len(arr) - 1)]
y = list(map(square, x))
z = list(map(double, y))

min_y = min(y)
max_z = max(z)
sorted_z = sorted(z)
print(f"min of y: {min_y}")
print(f"max of y: {max_z}")
print(f"sorted z: {sorted_z}")


# sorted_z = sorted(z)
# print(f"sorted z: {sorted_z}")
