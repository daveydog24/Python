# 1. 5
# 2. 10
# 3. 5
# 4. 5
# 5. 5, null  
# 6. Error
# 7. "25"
# 8. 

first_name = "Zen"
last_name = "Coder"
age = 27
x = (f"My name is {first_name} {last_name} and I am {age} years old.")

check_list = [x, 23, "Hi Kim", 1231, "Friend", 44, "This is a test"]

for x in check_list:
    if isinstance(x, str):
        x = x.split()
        for i in x:
            print(f"Single Word: {i}")
    elif isinstance(x, int):
        print (f"Number: {x}")

# x = x.split()
# for i in x:
#     if i.isalnum():
#         print(i)



