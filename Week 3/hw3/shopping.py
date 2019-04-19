with open('shopping.txt', 'r') as infile, open('results.txt', 'a') as outfile:
    # Read in the number of test cases and strip out un-needed elements
    test_case = int(infile.readline().strip())
    # Loop within the range of the test case
    for _ in range(test_case):
        # results will hold our items per family member; values will hold the value of each item (summed up at the end); weight will hold our total weights
        results = []
        weights = []
        values = []
        # List object for storing key/value pairs (key : [some array])
        item_list = {}
        items = int(infile.readline().strip())
        idx = 1
        # Generate key:value pairs for item_list
        for item in range(items):
            # Break up the line into price and weight
            price, weight = map(int, infile.readline().strip().split())
            # Store the array result above into the item_list object using price as the key
            item_list[price] = [weight, idx]
            idx += 1

        # Read in total number of family members
        # Write max carry weight to weights array.
        total_family_members = int(infile.readline().strip())
        for family_member in range(total_family_members):
            weights.append(int(infile.readline().strip()))
        # For each family member (using the stored weight) determine the highest valued item(s) they can carry.
        for weight in weights:
            sorted_price = sorted(item_list.keys())[::-1]
            m = 0
            p = 0
            temp = []

            # Get answer via greedy method. Max Price is added to an array of values.
            # Item number will be added to results array
            for i in range(len(item_list)):
                storage = []
                s = 0
                p = 0

                if item_list[sorted_price[i]][0] <= weight:
                    s = item_list[sorted_price[i]][0]
                    p = sorted_price[i]
                    storage += item_list[sorted_price[i]][1],

                for j in range(i+1, len(item_list)):
                    if item_list[sorted_price[j]][0] + s <= weight:
                        s += item_list[sorted_price[j]][0]
                        p += sorted_price[j]
                        storage += item_list[sorted_price[j]][1],

                if m < p:
                    m = p
                    temp = storage

            temp.sort()
            results.append(temp)
            values.append(m)
        # Write results to our outfile.
        outfile.write("Test Case: %d\n" % (_ + 1))
        outfile.write("Total Price: %d\n" % (sum(values)))
        outfile.write("Member Items:\n")
        # Grab recorded items for each person from results[] and write to outfile
        for i in range(len(results)):
            outfile.write("%d: %s\n" % (i + 1, " ".join(map(str, results[i]))))
    outfile.write('\n')