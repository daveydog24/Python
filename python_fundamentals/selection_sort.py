array = [1, 4, 6, 3, 8, 2, 9, 5]

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