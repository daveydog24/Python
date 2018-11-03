# ASCII Character Counting
# Created by David Wukelic

def ASCII(str1, str2, total):
    str1_test = isinstance(str1,str)
    str2_test = isinstance(str2,str)

    if str1_test == False or str2_test == False:
        print("Error: Content doesn't contain only strings")
        return -1

    one = list(str1)
    two = list(str2)
    total = total
    count = 0

    # sets up lists to make sure we always check the smaller lists so no errors occur
    if len(one) > len(two):
        temp = one
        one = two
        two = temp 

    # deletes matching characters
    while count < len(one):
        if one[count] == two[count]:
            del one[count]
            del two[count]
        else:
            count += 1
    
    '''
    conditional that ends function if lists are empty or uses 
    recursion to continue function till lists are empty
    then counts the character score and returns it
    '''

    if len(one) == 0:
        total += len(two)
        amount = 99
        final_sum = 0
        while total > 0:
            final_sum += amount
            total -= 1
        print(final_sum)
        return final_sum
    else:
        y = one[0]
        if y in two:
            two.remove(y)
        del one[0]
        total += 1
        one = ''.join(one)
        two = ''.join(two)
        ASCII(one, two, total)
        
str1 = 'bat'
str2 = 'coat'
print ASCII(str1, str2, 0)