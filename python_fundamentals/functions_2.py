# Functions_2
# Created by David Wukelic

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

sports_directory["basketball"] = "david"
print(sports_directory)


# loops through each index of x and checks each slot in each array and 
# changes the value of what youre looking for and what value you want to change it to
def changeValue(arr, value_in, value_out):
    outer_index = 0
    inner_index = 0
    for slot in arr:
        for slot_value in slot:
            if slot_value == value_in:
                arr[outer_index][inner_index] = value_out
            inner_index += 1
        inner_index = 0
        outer_index += 1
    return arr

print(changeValue(x, 2, 1511))
