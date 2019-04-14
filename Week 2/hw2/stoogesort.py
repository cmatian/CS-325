import datetime

filename = "data.txt"

"""
    Return an array of sorted integers using an stooge sort algorithm

    Keyword Arguments:
    array -- the unsorted array
"""
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

# Primary File Handling
with open(filename, "r") as file:
    for line in file:
        # Strip out the newline character from each line
        newline = line.rstrip('\n')
        # Convert string to an array of unsorted integers
        unsorted = map(int, newline.split(' '))
        # Pass unsorted array to merge sort function (ignoring the first index because we don't need it)
        sorted = stoogesort(unsorted[1:], 0, (len(unsorted[1:]) - 1))
        # Convert the result of sorted into a string
        string = ' '.join(str(e) for e in sorted)
        # Write each line to a text file called 'merge.txt'
        with open('stooge.out.txt', 'a') as insertFile:
            insertFile.write(string)
            insertFile.write('\n')
    # Generate a time stamp to the end of the 'merge.txt' file
    with open('stooge.out.txt', 'a') as insertFile:
        date = datetime.datetime.now()
        insertFile.write("Executed on: " + str(date))
        insertFile.write('\n\n')