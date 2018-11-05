array = [1, 4, 6, 3, 8, 2, 9, 5]

'''
Takes an array and checks each index slot of the array
it compares the index to the rest of the slots of the array until it finds the lowest number left unsorted
it then swaps that min num with the current index and will do this all the way through the list until each
index has been processed and sorted
'''
def selection_sort(arr):
    length = len(arr) - 1
    
    for index in range(0, length):
        count = index
        min_num = arr[count]
        min_index = count

        while count <= length:
            if arr[count] < min_num:
                min_index = count
                min_num = arr[count]
            count += 1
        arr[min_index], arr[index] = arr[index], min_num

    return arr

selection_sort(array)
print(array)