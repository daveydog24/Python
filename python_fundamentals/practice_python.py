'''
# This is a file to test python functions and techniques.
y = ["The boy went to the zoo", 5, 33, 12, "friends", 56, "winning", "testing", 11]
string = ""
total_sum = 0

for x in y:
    if isinstance(x, str):
        string += x + " "
    elif isinstance(x, int):
        total_sum += x
        
print(string)
print(total_sum)

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


capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country" 
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)

length_of_capitals = len(capitals)
string_of_capitals = str(capitals)
type_of_capitals = type(capitals)

print(length_of_capitals)
print(string_of_capitals)
print(type_of_capitals)

# reversing positively
arr = [1,3,5,7,9]
count = 1

while count <= len(arr):
    num = arr.pop(len(arr) - count)
    arr.append(num)
    count += 1
print(arr)

# reversing using negatives
count = -1
loops = len(arr) - 1
while loops > 0:
    count -= 1
    x = arr.pop(count)
    arr.append(x)
    loops -= 1
print(arr)

'''
stacks = 55

print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')
print("Testing " ? stacks >= 3 : "this" )
