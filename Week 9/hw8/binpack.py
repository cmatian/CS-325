
###### Fitting Algorithms #######

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

        print("Test case %d:\n\t\tFirst Fit: %d\n\t\tFirst Fit Decreasing: %d\n\t\tBest Fit: %d" % (x + 1, first_fit, decreasing_first_fit, best_fit))

