import datetime

filename = "data.txt"

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
    while(i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

# Primary File Handling
with open(filename, "r") as file:
    for line in file:
        # Strip out the newline character from each line
        newline = line.rstrip('\n')
        # Convert string to an array of unsorted integers
        unsorted = map(int, newline.split(' '))
        # Pass unsorted array to merge sort function (ignoring the first index because we don't need it)
        sorted = mergesort(unsorted[1:])

        string = ' '.join(str(e) for e in sorted)
        # Write each line to a text file
        with open('merge.txt', 'a') as mergeFile:
            mergeFile.write(string + '\n')
    with open('merge.txt', 'a') as mergeFile:
        date = datetime.datetime.now()
        mergeFile.write("Executed on: " + str(date) + '\n\n')