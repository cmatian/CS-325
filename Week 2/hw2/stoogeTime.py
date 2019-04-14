import time
import random

def stoogesort(array, min, max):
    if(array[min] > array[max]):
        temp = array[min]
        array[min] = array[max]
        array[max] = temp

    m = (max - min + 1) / 3
    if(m >= 1):
        stoogesort(array, min, max - m)
        stoogesort(array, min + m, max)
        stoogesort(array, min, max - m)

    return array

# Ranges to be used in the random array
n = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Run Merge Sort and collect the running time on the program
idx = 0
while (idx < len(n)):
    start = time.time()
    array = [random.random() for _ in range(n[idx])]
    min = 0
    max = len(array) - 1
    stoogesort(array, min, max)
    end = time.time()
    runtime = (end - start)
    print("N: " + str(idx + 1), "Time: " + str(runtime))
    idx += 1