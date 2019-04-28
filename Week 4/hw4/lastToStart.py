def activitySelection(v):
    # Sort the list by the finishing time
    v.sort(key = lambda x: x[2])
    # Capture length of list
    n = len(v)
    # Storage array for selected activities
    storage = []
    print("The following activities are selected")
    # Start with the last activity
    i = n - 1
    # Append the last activity by default since that's what we start with in a last-to-start algorithm
    storage.append(v[i][0])
    # Loop through the list in reverse order
    for idx, j in reversed(list(enumerate(v))):
        # Compare current activity's finish time to previous activity's start time.
        # If it's less than the start time than we push the activity number (j[0]) to the storage array.
        if j[2] <= v[i][1]:
            storage.append(j[0])
            # Set i to the enumerator (idx)
            i = idx
    # Return the storage array but reverse it first (to match the sample output solution)
    return list(reversed(storage))

with open('act.txt') as inFile:
    storage = []
    set = 1
    for line in inFile:
        # Clear trailing white spaces and \n characters
        line = line.rstrip()
        # Check if we've reached a line where there's no leading white space and the length of the storage array is greater than 0
        # This tells us that we've reached a new Set of data and should evaluate the current data set we collected.
        # The else condition will handle storage of the data into a list that's stored into the storage array.
        if ' ' not in line and len(storage) > 0:
            print("Set: " + str(set))
            # We need to test the first result of the array for data pollution.
            # The first loop will always append the # of activities, so we need to pass in an array that skips over the bad data
            if(len(storage[0]) > 1):
                result = activitySelection(storage[0:])
            else:
                result = activitySelection(storage[1:])
            print("Number of activities selected = " + str(len(result)))
            print("Activities: " + str(result) + '\n')
            set += 1
            storage = []
        else:
            storage.append([int(i) for i in line.split()])
    # A final pass that evaluates the rest of the data from the storage array.
    if len(storage) > 0:
        print("Set: " + str(set))
        result = activitySelection(storage)
        print("Number of activities selected = " + str(len(result)))
        print("Activities: " + str(result))