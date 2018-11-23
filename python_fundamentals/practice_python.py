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

stacks = 55
# python ternary operators
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')
# other language ternary operators
print('Coding Dojo' ? stacks >= 3 : 'You are not Coding Dojo!')

x = lambda num: num ** 2
print(x(5))

def invoker(callback_function):
    print(callback_function(2))

invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

def multiplier(num):
    start = num
    return lambda x: num * x

invoker(multiplier(10))

my_arr = [1,2,3,4,5]

def cubed(num):
    return num ** 3

# same thing but we dont have to make a stand alone function if we are only going to use it once
# this is a perfect example while anonymous functions with lambda are great
print(list(map(cubed, my_arr)))
print(list(map(lambda num: num ** 3, my_arr)))

# map(), reduce(), sort(), filter() are all great functions where lambda implenmentaion comes into play


# CLOSURE PRACTICE
# import logging
# logging.basicConfig(filename = 'example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        # logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
    # Necessary for closure to work (returning WITHOUT parenthesis)
    return log_func

def add(x,y):
    return x + y 

def sub(x,y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20, 10)

'''

import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)