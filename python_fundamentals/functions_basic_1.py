# 1. 5
# 2. 10
# 3. 5
# 4. 5
# 5. 5, null  
# 6. Error
# 7. "25"
# 8. 


# Variables for testing
first_name = "Zen"
last_name = "Coder"
age = 27
x = (f"My name is {first_name} {last_name} and I am {age} years old.")
check_list = [x, 23, "Hi Kim", 1231, "Friend", ["testing", "out", 3, "recursion is cool"], 44, "This is a test", ["words", 3], "hi"]

# Print Function
def print_out_everything_by_itself(check_list, count):
    for x in check_list:
        if isinstance(x, str):
            x = x.split()
            for i in x:
                print(f"Single Word: {i}")
        elif isinstance(x, int):
            print (f"Number: {x}")
        elif isinstance(x, list):
            count += 1
            print("going into recursion, count number:", count)
            print_out_everything_by_itself(x, count)

# invoking the function
print_out_everything_by_itself(check_list, 0)
            
        



