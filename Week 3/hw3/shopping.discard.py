# Knapsack Algorithm
# n = total number of items
# m = current family member carry capacity
def knapsack(prices_array, weights_array, n, m, container):

    # Build a table and initialize spots to 0
    # x = rows, y = columns
    # m = x, n = y
    table = [[0 for y in range(m + 1)] for x in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if(i == 0 or j == 0):
                table[i][j] = 0
            elif(weights_array[i - 1] <= j):
                table[i][j] = max(prices_array[i - 1] + table[i - 1][j - weights_array[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    results = table[n - 1][m - 1]
    weight = m
    idx = n

    while(idx > 0 and results > 0):
        idx -= 1
        if(results == table[idx - 1][weight]):
            continue
        else:
            container.append(idx)
            results -= prices_array[idx - 1]
            weight -= weights_array[idx - 1]

    return table[n - 1][m - 1]



# Main Code Body
with open('shopping.txt', 'r') as infile, open('shopping.out', 'w') as outfile:
    test_cases = int(infile.readline().strip())
    for _ in range (test_cases):
        # Weight and Price arrays are initialized as empty for each test case
        weights = []
        prices = []

        # Read in the number of items from the second line of that test case
        total_items = int(infile.readline().strip())
        for item in range(total_items):
            # Read each line into an array
            storage = map(int, infile.readline().strip().split(' '))
            # Break up the results of the storage array into the weights[] and prices[] arrays
            prices.append(storage[0])
            weights.append(storage[1])

        # Read in the number of family members and for each person evaluate them against the knapsack algorithm
        total_family_members = int(infile.readline().strip())

        # Create a quick 2d array based on the total items.
        # The total weight capacity is 1 <= m <= 200
        items_to_hold = [[0 for y in range(201)] for x in range(total_items)]

        max_price = 0
        for family_member in range(total_family_members):
            cap = int(infile.readline().strip())
            # Track the max price of items that each family member can carry
            max_price += knapsack(prices, weights, total_items, cap, items_to_hold)

        # Print out results to file
        outfile.write("Test Case: %d\n" % (_ + 1))
        outfile.write("Total Price: %d\n" % (max_price))
        outfile.write("Member Items:\n")




