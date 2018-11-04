'''
# function practice 1
# created by David Wukelic

# Create beCheerful().  Within it, print string "good morning!" 98 times.
print("*"*80)
def beCheerful(name='', repeat=1):
	print(f"good morning {name}\n"*repeat)
beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")
# helpful tips for the next assignment
import random
print(random.random()) # returns a random floating number between 0.000 to 1.000
print(random.random()*50) # returns a float between 0.000 to 50.000
int( 3.654 ) # returns 3
round( 3.654 ) # returns 4

# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().
'''

def randInt(min = 0, max = 100):
    import random
    min_num = min
    max_num = max
    print(min_num)
    print(max_num)

randInt()


