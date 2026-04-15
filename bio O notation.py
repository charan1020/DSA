# O(1) is constant time complexity, which means that the time taken to execute the algorithm does not depend on the size of the input data. It is the most efficient time complexity, as it indicates that the algorithm will always take the same amount of time to execute, regardless of the input size. Examples of O(1) algorithms include accessing an element in an array by index or performing a simple arithmetic operation.
# O(n) is linear time complexity, which means that the time taken to execute the algorithm increases linearly with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm also doubles. Examples of O(n) algorithms include iterating through an array or a list to find a specific element or to calculate the sum of all elements.
# O(n^2) is quadratic time complexity, which means that the time taken to execute the algorithm increases quadratically with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a factor of four. Examples of O(n^2) algorithms include nested loops that iterate through all elements of a 2D array or list.
# O(log n) is logarithmic time complexity, which means that the time taken to execute the algorithm increases logarithmically with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a constant amount. Examples of O(log n) algorithms include binary search and certain sorting algorithms like merge sort and quicksort.
# O(n log n) is linearithmic time complexity, which means that the time taken to execute the algorithm increases as a combination of linear and logarithmic factors with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a factor of n log n. Examples of O(n log n) algorithms include efficient sorting algorithms like merge sort and quicksort.
# O(2^n) is exponential time complexity, which means that the time taken to execute the algorithm increases exponentially with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a factor of 2^n. Examples of O(2^n) algorithms include certain recursive algorithms, such as the naive implementation of the Fibonacci sequence.
# O(n!) is factorial time complexity, which means that the time taken to execute the algorithm increases factorially with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a factor of n!. Examples of O(n!) algorithms include certain brute-force algorithms, such as generating all permutations of a set of items.
#O(2n) is exponential time complexity, which means that the time taken to execute the algorithm increases exponentially with the size of the input data. In other words, if the input size doubles, the time taken to execute the algorithm increases by a factor of 2^n. Examples of O(2n) algorithms include certain recursive algorithms, such as the naive implementation of the Fibonacci sequence.

#o(1)
from pandas import merge
arr=[1, 2, 3, 4, 5]
print(arr[2]) # O(1)

#o(n)
arr=[1, 2, 3, 4, 5]
for i in arr:
    print(i) # O(n)

#o(n^2)
arr=[[1, 2], [3, 4], [5, 6]]
for i in arr:
    for j in i:
        print(j) # O(n^2)

#o(log n)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # O(log n)

#o(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half) # O(n log n)    

#o(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) # O(2^n)

#o(n!)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) # O(n!)   

#O(2n)
def power_of_two(n):
    if n == 0:
        return 1
    return 2 * power_of_two(n-1) # O(2n)

