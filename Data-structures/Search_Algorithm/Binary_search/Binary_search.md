
# Binary Search Explanation

## Purpose:
This script implements the **Binary Search** algorithm, which is an efficient way to search for a specific element within a **sorted array**. It repeatedly divides the search interval in half and checks if the middle element is the target value. If the target is found, the index is returned; otherwise, the search space is narrowed until the target is located or the array is exhausted.

## How the Code Works:
1. **Initialization**:
   The array `arr` is pre-defined as `[11, 12, 13, 14, 15, 16, 17, 18, 19]`, and the user is prompted to input a number to search for in this array.

2. **Binary Search Logic**:
   - The function `binary_search(arr, search)` is called with two parameters:
     - `arr`: the sorted list of numbers.
     - `search`: the number the user wants to find.
   - Two variables are initialized:
     - `left = 0`: represents the starting index of the array.
     - `right = len(arr) - 1`: represents the last index of the array.
     
3. **Search Loop**:
   The `while` loop continues as long as `left <= right`, meaning there's still a valid search interval:
   - The middle index `m` is calculated using the formula `m = (left + right) // 2`.
   - The value at the middle index is compared to the target `search`:
     - If `arr[m] == search`: The target is found, and the index `m` is printed with the message "the index of the number is: m".
     - If `arr[m] < search`: The target is in the right half of the array, so `left = m + 1` is set.
     - If `arr[m] > search`: The target is in the left half of the array, so `right = m - 1` is set.
     
4. **Exiting the Loop**:
   - If the element is not found by the time the search space is narrowed down, the loop terminates, and the message "The number you entered is not in the list" is printed.

## Example Usage:
For an input of `search = 14`, the program will output:
```
the index of the number is: 3
```
For an input of `search = 20`, the program will output:
```
The number you entered is not in the list
```

## Complexity:
- **Time Complexity**: O(log n) because the search space is halved at each step.
- **Space Complexity**: O(1) as the algorithm uses a constant amount of extra space.

## Conclusion:
This implementation demonstrates a classic example of binary search in a sorted array, which is efficient and commonly used in various algorithms for searching in large datasets.
