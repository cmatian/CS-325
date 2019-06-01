import random
import timeit
from random import randint

# Binpacking Functions: Firstfit, firstFitDecreasing, and bestFit
def firstFit(a, b, c):
    result = 0
    bins = [a] * b
    capacity = a
    items = b
    weights = c

    # Loop through each item
    for i in range(items):
        idx = 0
        # Find a bin to place it into
        while(idx < result):
            if(bins[idx] >= weights[i]):
                bins[idx] = bins[idx] - weights[i]
                break
            idx += 1
        # If we didn't find a bin, find a new bin to place it into
        if(idx == result):
            bins[result] = capacity - weights[i]
            result += 1

    return result

# Same as above function but we simply sort the data before iterating through the data
def firstFitDecreasing(a, b, c):
    return firstFit(a, b, sorted(c, reverse=True))

# Similar to firstFit but we're looking for the tightest possible bin to fit the item into first
def bestFit(a, b, c):
    result = 0
    bins = [a] * b
    capacity = a
    items = b
    weights = c

    # Loop through each item
    for i in range(items):
        idx = 0
        min = capacity
        index_of_best_bin = 0
        # Find the tightest possible bin to place the item into
        while(idx < result):
            if(bins[idx] >= weights[i] and bins[idx] - weights[i] < min):
                index_of_best_bin = idx
                min = bins[idx] - weights[i]
            idx += 1
        # If we didn't find a bin, find a new tighter bin to place it into
        if(min == capacity):
            bins[result] = capacity - weights[i]
            result += 1
        else:
            bins[index_of_best_bin] -= weights[i]

    return result

# Function definition for generating a random sized list of random, positive integers
def generateList():
    random_int = random.randint(5, 20) # List length range
    rand_list = [randint(1, 20) for _ in range(random_int)] # Integer value range
    return rand_list

# Main Storage List for the lists we randomly generate
itemList = []

# Generate the random lists and append them to our itemList storage list
for x in range(20):
    itemList.append(generateList())

for i, x in enumerate(itemList):
    # Capture time for each function
    ff_start = timeit.default_timer()
    first_fit = firstFit(max(x), len(x), x)
    ff_end = timeit.default_timer()
    ff_time = (ff_end - ff_start)

    ffd_start = timeit.default_timer()
    decreasing_first_fit = firstFitDecreasing(max(x), len(x), x)
    ffd_end = timeit.default_timer()
    ffd_time = (ffd_end - ffd_start)

    bf_start = timeit.default_timer()
    best_fit = bestFit(max(x), len(x), x)
    bf_end = timeit.default_timer()
    bf_time = (bf_end - bf_start)

    print("--- Test case %d ---" % (i + 1))
    print("List: %s, Length: %d" % (x, len(x)))
    print("\tFirst-Fit:")
    print("\t\tBins: %d, Time: %0.10f\n" % (first_fit, ff_time))
    print("\tFirst-Fit-Decreasing:")
    print("\t\tBins: %d, Time: %0.10f\n" % (decreasing_first_fit, ffd_time))
    print("\tBest-Fit:")
    print("\t\tBins: %d, Time: %0.10f\n" % (best_fit, bf_time))

