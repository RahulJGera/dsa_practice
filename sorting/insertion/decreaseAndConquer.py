#!/usr/bin/python3

# Decrease and Conquer Approach for Insertion sort
# Example array of items Unsorted
#    {
#        "arr": [5, 8, 3, 9, 4, 1, 7]
#    }
# Sorted output should look like below
#    [1, 3, 4, 5, 7, 8, 9]

def insertion_sort(arr):
    for idx in range(len(arr)):
        temp = arr[idx]
        rIdx = idx - 1
        while rIdx >= 0 and temp < arr[rIdx]:
            arr[rIdx + 1] = arr[rIdx]
            rIdx -= 1
        arr[rIdx + 1] = temp
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]

print(insertion_sort(arr))
