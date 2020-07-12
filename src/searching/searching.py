def linear_search(arr, target):
    for num in range(len(arr)):
        if arr[num] == target:
            return num


    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)

    found = False
    while start <= end and not found:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            found = True
            return middle_index

        # else if sort number closer to start/ end

        elif target < arr[middle_index]:
            end = middle_index - 1
        elif target > arr[middle_index]:
            start = middle_index + 1


    return -1  # not found
