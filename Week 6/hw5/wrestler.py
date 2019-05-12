import sys

with open(sys.argv[1], 'r') as inFile:
    # Create a dictionary to store our key/value pairs
    roster = {}
    flag = 1

    # Read in first line of the input file (number of wrestler's to process)
    n = int(inFile.readline().rstrip())

    # Loop through each wrestler name using n as the range
    for i in range(n):
        name = inFile.readline().rstrip()
        color = 'none' if flag == 0 else 'blue'

        # First loop of the wrestler will set the flag to 1 (we only want the first looped wrestler to be a babyface - blue)
        flag = 0

        roster[name] = color

    # After reading in each wrestler line, the next line will be the number of rivalries
    n = int(inFile.readline().rstrip())

    # Loop through each rivalry
    for i in range(n):
        line = inFile.readline().rstrip()
        # Split each line into an array of two items consisting of the rivalry)
        rivalry = [str(i) for i in line.split()]
        r1 = rivalry[0]
        r2 = rivalry[1]

        # Main conditional blocks for evaluating each wrestler pairing
        # We use a key/value pair format to quickly access and evaluate the color of each wrestler against the specified condition
        if(roster[r1] == 'none' and roster[r2] == 'none'):
            roster[r1] = 'blue'
            roster[r2] = 'red'
            continue

        if(roster[r1] == 'none' and roster[r2] != 'none'):
            roster[r1] = 'blue' if roster[r2] == 'red' else 'red'
            continue

        if (roster[r2] == 'none' and roster[r1] != 'none'):
            roster[r2] = 'red' if roster[r1] == 'blue' else 'blue'
            continue

        if(roster[r1] == 'blue' and roster[r2] == 'none'):
            roster[r2] = 'red'
            continue

        if(roster[r1] == 'red' and roster[r2] == 'none'):
            roster[r2] = 'blue'
            continue

        if(roster[r1] == 'blue' and roster[r2] == 'blue'):
            exit('No - Impossible')

        if(roster[r1] == 'red' and roster[r2] == 'red'):
            exit('No - Impossible')

    babyFace = []
    heel = []
    for i in roster:
        if roster[i] == 'blue':
            babyFace.append(i)
        else:
            heel.append(i)

    print('Yes - possible')
    print('Babyfaces:'),
    for i in babyFace:
        print(i),
    print('\nHeels:'),
    for i in heel:
        print(i),


