"""
Merge Sort

-Two implementations, one in place
"""

import numpy as np




def combine_arrays( arr_l, arr_r ):
    num_elements = len( arr_l ) + len( arr_r )
    merged_arr = np.array([0] * num_elements)
    
    left_index = 0
    right_index = 0  # Could represent as array, merging more than 2 lists
    i=0
    while left_index is not None and right_index is not None:
        if arr_l[left_index] <= arr_r[right_index]:  # bias left array
            merged_arr[i] = arr_l[left_index]
            left_index = increment_or_none(index=left_index + 1, array=arr_l)
        else:
            merged_arr[i] = arr_r[right_index]
            right_index = increment_or_none(index=right_index + 1, array=arr_r)
        i += 1


    if left_index is None:
        # fill from right array
        while right_index is not None:
            merged_arr[i] = arr_r[right_index]
            right_index = increment_or_none(index=right_index + 1, array=arr_r)
            i += 1
    if right_index is None:
        # fill from left array
        while left_index is not None:
            merged_arr[i] = arr_l[left_index]
            left_index = increment_or_none(index=left_index + 1, array=arr_l)
            i += 1

    return merged_arr




def increment_or_none(index, array):
    try:
        array[index]
        test = True
    except:
        test = False

    if test:
        return index
    else:
        return None




def split_array(array):
    midpoint = int(len(array)/2)
    return array[0:midpoint], array[midpoint:]




def merge_sort(arr):
    if len(arr) > 1:
        array_1, array_2 = split_array(arr)
        arr = combine_arrays(merge_sort(array_1), merge_sort(array_2))
    return list(arr)


if __name__ == "__main__":
    test_arr = [1,4,5,7,2,8,5,3, 2, 524, 41, 432]

    print(merge_sort(test_arr))