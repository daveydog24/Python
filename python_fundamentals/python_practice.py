# This is a file to test python functions and techniques.

def ASCII(str1, str2, total):
    one = list(str1)
    two = list(str2)
    total = total
    count = 0

    if len(one) > len(two):
        temp = one
        one = two
        two = temp 

    while count < len(one):
        if one[count] == two[count]:
            del one[count]
            del two[count]
        else:
            count += 1

        
str1 = 'boat'
str2 = 'coat'
print ASCII(str1, str2, 0)