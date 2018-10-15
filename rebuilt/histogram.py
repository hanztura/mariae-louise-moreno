from collections import Counter

n = 2
# get test cases
multiplier = n
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)

# output
transformed_input_test_cases = [input_test_cases[i:i+n] for i in range(0, len(input_test_cases), n)]
for test_case in transformed_input_test_cases:
    bin_size = int(test_case[0])
    data = test_case[1].split()
    data = [int(i) for i in data]  # transform into integers

    lowest_data = min(data)
    highest_data = max(data)
    bins_min_points = list(range(lowest_data, highest_data, bin_size))
    if (max(bins_min_points) + bin_size) < highest_data:
        bins_min_points.append(max(bins_min_points) + bin_size)

    # counted_data = data_counter(data)
    counter = Counter(data)
    counted_data = dict(counter)

    # create bins
    bins = []
    bin_count = []
    for i in bins_min_points:
        _bin = (i, i+bin_size - 1)
        bins.append(_bin)
        bin_count.append(0)

    for key in counted_data:
        value = counted_data[key]
        for (i, _bin) in enumerate(bins):
            low = _bin[0]
            high = _bin[1]
            if key >= low and key <= high:
                bin_count[i] += value
                break

    for (i, _bin) in enumerate(bins):
        low = _bin[0]
        high = _bin[1]
        value = bin_count[i]
        string = '{}-{} {}'.format(low, high, value)
        print(string)

    print()