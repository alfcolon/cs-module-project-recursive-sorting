# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left_arr, right_arr):
    elements = len(left_arr) + len(right_arr)
    merged_arr = [0] * elements
    left_len = len(left_arr)
    right_len = len(right_arr)
    
    # Start populating the merged array in ascending order
    merged_index = 0
    left_index = 0
    right_index = 0
    while left_index < left_len and right_index < right_len:
        left_value = left_arr[left_index]
        right_value = right_arr[right_index]
        if left_value == right_value:
            merged_arr[merged_index] = left_value
            merged_arr[merged_index + 1] = right_value
            merged_index += 2
            left_index += 1
            right_index += 1
        elif left_value < right_value:
            merged_arr[merged_index] = left_value
            left_index += 1
            merged_index += 1
        elif right_value < left_value:
            merged_arr[merged_index] = right_value
            right_index += 1
            merged_index += 1
        
    # Add any remaining left_array values to the merged array
    while left_index < left_len:
        merged_arr[merged_index] = left_arr[left_index]
        left_index += 1
        merged_index += 1
    # Add any remaining right_array values to the merged array
    while right_index < right_len:
        merged_arr[merged_index] = right_arr[right_index]
        right_index += 1
        merged_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Recur if length is greater than one
    arrLen = len(arr)
    if arrLen > 1:
        middle_index = arrLen / 2
        left_arr = arr[:middle_index]
        right_arr = arr[middle_index:]
        
        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)
        
        merged_array = merge(left_arr, right_arr)
        return merged_array
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#[134] [215]
# 1 3 4 4 1 5
# 1 3 3 4 1 5
# 1 2 3 4 1 5
def merge_in_place(arr, start, mid, end):
    # Sort array, adding elements in ascending order
    arr_index = start
    left_index = start
    right_index = mid + 1
    
    if arr[mid] <= arr[right_index]:
           return
           
    while left_index <= mid and right_index <= end:
        left_value = arr[left_index]
        right_value = arr[right_index]
        if left_value <= right_value:
            left_index += 1
        else:
            # Shift elements over one place from left_index + 1 to and including the right_index
            shift_index = right_index
            while (shift_index != left_index):
                arr[shift_index] = arr[shift_index - 1]
                shift_index -= 1
            # Now update the value of the left_index
            arr[left_index] = right_value
            # Update the indexes
            left_index += 1
            mid += 1
            right_index += 1

def merge_sort_in_place(arr, start, end):
    if start < end:
        middle_index = start + (end - start) // 2
        # Recur left
        merge_sort_in_place(arr, start, middle_index)
        # Recur right
        merge_sort_in_place(arr, middle_index + 1, end)

        merge_in_place(arr, start, middle_index, end)



#def merge(arr, start, mid, end):
#    start2 = mid + 1;
#
#    # If the direct merge is already sorted
#    if (arr[mid] <= arr[start2]):
#        return;
#
#    # Two pointers to maintain start
#    # of both arrays to merge
#    while (start <= mid and start2 <= end):
#
#        # If element 1 is in right place
#        if (arr[start] <= arr[start2]):
#            start += 1;
#        else:
#            value = arr[start2];
#            index = start2;
#
#            # Shift all the elements between element 1
#            # element 2, right by 1.
#            while (index != start):
#                arr[index] = arr[index - 1];
#                index -= 1;
#
#            arr[start] = value;
#
#            # Update all the pointers
#            start += 1;
#            mid += 1;
#            start2 += 1;
#
#'''
#* l is for left index and r is right index of
#the sub-array of arr to be sorted
#'''
#def mergeSort(arr, l, r):
#    if (l < r):
#
#        # Same as (l + r) / 2, but avoids overflow
#        # for large l and r
#        m = l + (r - l) // 2;
#
#        # Sort first and second halves
#        mergeSort(arr, l, m);
#        mergeSort(arr, m + 1, r);
#
#        merge(arr, l, m, r);
