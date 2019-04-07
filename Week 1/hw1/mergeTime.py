import time
import random
"""
    Return an array of sorted integers

    Keyword Arguments:
    array -- the unsorted array
"""
def mergesort(array):
    length = len(array)

    # Array only contains one value
    if (length < 2):
        return array

    # Set the middle of the array and split the array into two based on the midpoint (left and right)
    mid = length // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    return merge(left, right)

"""
    Return a result consisting of two merged left and right arrays

    Keyword Arguments:
    left -- the left half of an array
    right -- the right half of an array
"""
def merge(left, right):
    result = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

# Ranges to be used in the random array
n = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

# Run Merge Sort and collect the running time on the program
idx = 0
while (idx < len(n)):
    start = time.time()
    mergesort([random.random() for _ in range(n[idx])])
    end = time.time()
    runtime = (end - start)
    print("N: " + str(idx + 1), "Time: " + str(runtime))
    idx += 1

