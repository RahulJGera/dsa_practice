#!/usr/bin/python3

# BruteForce Approach for bubble sort
# Example array of items Unsorted
#    {
#        "arr": [5, 8, 3, 9, 4, 1, 7]
#    }
# Sorted output should look like below
#    [1, 3, 4, 5, 7, 8, 9]

def bubble_sort(arr):
    for _ in range(len(arr) - 1):
        endIdx = len(arr) - 1
        while endIdx > 0:
            if arr[endIdx] < arr [endIdx - 1]:
                arr[endIdx], arr[endIdx - 1] = arr[endIdx - 1], arr[endIdx]
            endIdx -= 1
    return arr
arr = [5, 8, 3, 9, 4, 1, 7]

print(bubble_sort(arr))
