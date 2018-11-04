array = [1, 4, 6, 3, 8, 2, 9, 5]

def bubble_sort(arr):
    length = len(arr) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for index in range(length):
            if arr[index] > arr[index+1]:
                is_sorted = False
                arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr

bubble_sort(array)
print(array)

