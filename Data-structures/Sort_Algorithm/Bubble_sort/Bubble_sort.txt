
Bubble Sort Explanation
=======================
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly compares adjacent elements in an array 
and swaps them if they are in the wrong order. It ensures that after each pass, the largest unsorted element 
is placed in its correct position.

Algorithm Steps:
1. Traverse the array multiple times (one pass per loop iteration).
2. In each pass, compare adjacent elements.
3. Swap the elements if the current element is greater than the next element.
4. Repeat the process until no swaps are needed.

Characteristics:
- Algorithm Type: Comparison-based sorting algorithm.
- Time Complexity:
  - Best case (already sorted): O(n)
  - Worst case (reversed): O(n^2)
  - Average case: O(n^2)
- Space Complexity: O(1) (in-place sorting, no additional memory used).
- Stability: Stable (does not change the order of equal elements).

Pseudocode for Bubble Sort:
===========================
BUBBLE SORT(arr)
    Input: arr (an array of n elements)
    Output: arr (sorted in ascending order)

    For j from 0 to len(arr) - 1 do:
        For i from 0 to len(arr) - 2 do:
            If arr[i] > arr[i + 1] then:
                Swap arr[i] and arr[i + 1]
            End If
        End For
    End For

    Print arr

Example Walkthrough:
====================
Input: [1, 2, 5, 3, 8, 3, 4, 6, 4]

Iteration Details:
- Pass 1: [1, 2, 3, 5, 3, 4, 6, 4, 8]
- Pass 2: [1, 2, 3, 3, 4, 5, 4, 6, 8]
- Pass 3: [1, 2, 3, 3, 4, 4, 5, 6, 8]
- Pass 4: [1, 2, 3, 3, 4, 4, 5, 6, 8] (No swaps required, array is sorted.)

Output: [1, 2, 3, 3, 4, 4, 5, 6, 8]
