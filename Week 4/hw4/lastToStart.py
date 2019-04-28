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
    st = []
    sn = 1
    for line in inFile:
        # Clear trailing white spaces and \n characters
        l = line.rstrip()
        # Check if we've reached a line where there's no leading white space and the length of the st array is greater than 0
        # This tells us that we've reached a new Set of data and should evaluate the current data set we collected.
        # The else condition will handle storage of the data into a list that's stored into the st array.
        if ' ' not in l and len(st) > 0:
            print("Set: " + str(sn))
            # We need to test the first result of the array for data pollution.
            # The first loop will always append the # of activities, so we need to pass in an array that skips over the bad data
            if(len(st[0]) > 1):
                sol = activitySelection(st[0:])
            else:
                sol = activitySelection(st[1:])
            print("Number of activities selected = " + str(len(sol)))
            print("Activities: " + str(sol) + '\n')
            sn += 1
            st = []
        else:
            st.append([int(i) for i in l.split()])
    # A final pass that evaluates the rest of the data from the st array.
    if len(st) > 0:
        print("Set: " + str(sn))
        sol = activitySelection(st)
        print("Number of activities selected = " + str(len(sol)))
        print("Activities: " + str(sol))