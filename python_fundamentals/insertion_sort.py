# Insertion Sort
# Created by: David Wukelic

def insertion_sort(arr):
    length = len(arr) - 1
    index = 1

    # continue loop function till all indexes have been checked
    while index <= length:
        curr_value = arr[index]
        temp_index = index

        # swaps values until the current index is higher than its previous
        while curr_value < arr[temp_index - 1]:
            arr[temp_index], arr[temp_index - 1] = arr[temp_index - 1], arr[temp_index]
            temp_index -= 1

        index += 1

    return arr

unsorted_array = [1, 4, 6, 3, 8, 2, 9, 5]
print(insertion_sort(unsorted_array))
