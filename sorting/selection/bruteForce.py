#!/usr/bin/python3

# BruteForce Approach for selection sort
# Example array of items Unsorted
#    {
#        "arr": [5, 8, 3, 9, 4, 1, 7]
#    }
# Sorted output should look like below
#    [1, 3, 4, 5, 7, 8, 9]

def selection_sort(arr):
    for idx in range(0,len(arr)):
        minValue = arr[idx]
        minIdx = idx
        for rIdx in range(idx+1, len(arr)):
            if arr[rIdx] < minValue:
                minValue = arr[rIdx]
                minIdx = rIdx
        if minValue != arr[idx]:
            arr[idx], arr[minIdx] = arr[minIdx], arr[idx]
    return arr

arr = [5, 8, 3, 9, 4, 1, 7]

print(selection_sort(arr))
