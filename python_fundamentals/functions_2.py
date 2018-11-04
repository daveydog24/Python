'''
# Functions_2
# Created by David Wukelic


**************************************** SECTION 1 ***********************************************

x = [ [5,2,3], [10,8,9] ] 

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

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# ability to change names based on index
def change_last_name(student_list, index, new_name):
    student_list[index]["last_name"] = new_name
    return student_list

students = change_last_name(students, 0, "Wukelic")

def change_first_name(student_list, index, new_name):
    student_list[index]["first_name"] = new_name
    return student_list

students = change_first_name(students, 0, "David")

# ability to change names given only the name
def change_name(student_list, name_to_change, new_name):
    for students in student_list:
        if students["first_name"] == name_to_change:
            students["first_name"] = new_name
        elif students["last_name"] == name_to_change:
            students["last_name"] = new_name
    return student_list

print(students)
change_name(students, "David", "Kimberly")
print(students)


**************************************** SECTION 2 ***********************************************
'''
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary1(students):
    for student in students:
        first_name = student["first_name"] 
        last_name = student["last_name"]
        print(f"first_name - {first_name}, last_name - {last_name}")

def iterateDictionary2(word, students):
    for student in students:
        for key, value in student.items():
            if key == word:
                print(value)
            elif value == word:
                print(value)

iterateDictionary2('last_name', students)
    
    



# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# sports_directory["basketball"] = "david"
# print(sports_directory)