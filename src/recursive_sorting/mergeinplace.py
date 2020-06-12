# Python program in-place Merge Sort 
  
# Merges two subarrays of arr. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
# Inplace Implementation 

# Adapted from https://www.geeksforgeeks.org/in-place-merge-sort/


def merge(arr, start, mid, end): 
    start2 = mid + 1
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
              
            arr[start] = value; 
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
    
''' 
* l is for left index and r is right index of 
the sub-array of arr to be sorted 
'''
def merge_sort_in_place(arr, l, r): 
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
  
        merge(arr, l, m, r)
    return arr


if __name__ == "__main__":
    arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    print(merge_sort_in_place(
        arr1, 0, len(arr1)-1
    ))