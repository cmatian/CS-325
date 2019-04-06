import datetime
filename = "data.txt"

"""
    Return an array of sorted integers using an insertion sort algorithm

    Keyword Arguments:
    array -- the unsorted array
"""
def insertsort(array):

    i = 0
    length = len(array)

    while(i < length):
        temp = array[i]
        j = i
        while(j > 0 and temp < array[j - 1]):
            array[j] = array[j - 1]
            j -= 1

        array[j] = temp
        i += 1

    return array

# Primary File Handling
with open(filename, "r") as file:
    for line in file:
        # Strip out the newline character from each line
        newline = line.rstrip('\n')
        # Convert string to an array of unsorted integers
        unsorted = map(int, newline.split(' '))
        # Pass unsorted array to merge sort function (ignoring the first index because we don't need it)
        sorted = insertsort(unsorted[1:])
        # Convert the result of sorted into a string
        string = ' '.join(str(e) for e in sorted)
        # Write each line to a text file called 'merge.txt'
        with open('insert.txt', 'a') as insertFile:
            insertFile.write(string + '\n')
    # Generate a time stamp to the end of the 'merge.txt' file
    with open('insert.txt', 'a') as insertFile:
        date = datetime.datetime.now()
        insertFile.write("Executed on: " + str(date) + '\n\n')