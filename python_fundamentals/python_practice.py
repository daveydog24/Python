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

    if len(one) == 0:
        total += len(two)
        amount = 99
        final_sum = 0
        while total > 0:
            final_sum += amount
            total -= 1
        print(final_sum)
        return final_sum
        
str1 = 'boat'
str2 = 'coat'
print ASCII(str1, str2, 0)