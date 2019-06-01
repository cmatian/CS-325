import timeit

###### Fitting Algorithms ######
# First Fit
# a = capacity, b = total number of items, c = weights of items
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


# Driver
with open('bin.txt', 'r') as inFile:
    # Read in the number of test cases
    line = int(inFile.readline().rstrip())

    # Loop through the range of test cases
    for x in range(line):
        # Read in the capacity of each bag
        capacity = int(inFile.readline().rstrip())

        # Read in the number of items
        item_total = int(inFile.readline().rstrip())

        # Create an array from the line of integers (this represents the weight of each item)
        item_weights = map(int, inFile.readline().rstrip('\n').split(' '))

        # Pass in each variable to the three algorithms and grab their results
        first_fit = firstFit(capacity, item_total, item_weights)
        decreasing_first_fit = firstFitDecreasing(capacity, item_total, item_weights)
        best_fit = bestFit(capacity, item_total, item_weights)

        # Capture time for each function
        ff_start = timeit.default_timer()
        firstFit(capacity, item_total, item_weights)
        ff_end = timeit.default_timer()
        ff_time = (ff_end - ff_start)

        ffd_start = timeit.default_timer()
        firstFitDecreasing(capacity, item_total, item_weights)
        ffd_end = timeit.default_timer()
        ffd_time = (ffd_end - ffd_start)

        bf_start = timeit.default_timer()
        bestFit(capacity, item_total, item_weights)
        bf_end = timeit.default_timer()
        bf_time = (bf_end - bf_start)

        print("--- Test case %d ---" % (x + 1))
        print("\tFirst-Fit:")
        print("\t\tBins: %d, Time: %0.10f\n" % (first_fit, ff_time))
        print("\tFirst-Fit-Decreasing:")
        print("\t\tBins: %d, Time: %0.10f\n" % (decreasing_first_fit, ffd_time))
        print("\tBest-Fit:")
        print("\t\tBins: %d, Time: %0.10f\n" % (best_fit, bf_time))
