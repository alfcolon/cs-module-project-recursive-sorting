# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    
    middle_index = (start + end) // 2
    middle_value = arr[middle_index]
    
    if middle_value == target:
        return middle_index
    elif target < middle_value:
        return binary_search(arr, target, start, middle_index - 1)
    else:
        return binary_search(arr, target, middle_index + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    ascending = arr[end] > arr[start]
    while start <= end:
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        if target == middle_value:
            return middle_index
        if target < middle_value:
            if ascending:
                end = middle_index - 1
            else:
                start = middle_index + 1
        elif target > middle_value:
            if ascending:
                start = middle_index + 1
            else:
                end = middle_index - 1
    return -1
