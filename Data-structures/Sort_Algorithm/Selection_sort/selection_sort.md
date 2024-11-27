Selection Sort Implementation in Python
========================================

Description:
------------
This program demonstrates the implementation of the Selection Sort algorithm in Python.
Selection Sort is a simple, comparison-based sorting algorithm. It sorts an array by 
repeatedly finding the smallest element from the unsorted portion of the array and 
placing it at the beginning.

How It Works:
-------------
1. Start with the first element of the array.
2. Find the smallest element in the unsorted part of the array.
3. Swap the smallest element with the current element.
4. Repeat the process for the rest of the array until it is sorted.

Time Complexity:
----------------
- Best case: O(n^2)
- Average case: O(n^2)
- Worst case: O(n^2)

Space Complexity:
-----------------
- O(1) (In-place sorting)

Code:
-----
```python
def selection_sort(arr):
    for i in range(0, len(arr)):        
        min_index = i        
        for j in range(i + 1, len(arr)):            
            if arr[j] < arr[min_index]:
                min_index = j               
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

# Test the function
arr = [19, 3, 2, 5, 56, 28, 49, 12, 23, 34, 43, 65, 10]
selection_sort(arr)
