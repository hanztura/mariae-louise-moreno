multiplier = 1
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)


# output
for test_case in input_test_cases:
    test_case = test_case.split()
    start_num = int(test_case[0])
    end_count = int(test_case[1])

    reads = []
    reads.append(start_num)
    _counter = 1
    while True:
        if _counter > end_count:
            break

        # read
        string_current_number_to_read = str(reads[_counter - 1])
        # current_read = inventory_reader(string_current_number_to_read)
        data = []
        current_chars = ''
        for char in string_current_number_to_read:
            if current_chars == '' or current_chars[0] == char:
                current_chars += char
            else:
                data.append(current_chars)
                current_chars  = char

        data.append(current_chars)
        current_chars = ''

        # count
        data_count = []
        unique_chars = []
        for i in data:
            count = len(i)
            unique_chars.append(i[0])
            data_count.append(count)

        current_read = ''
        for (i, count) in enumerate(data_count):
            _string = unique_chars[i]
            read_string = '{}{}'.format(count, _string)
            current_read += read_string

        reads.append(current_read)
        _counter += 1

    print(reads[end_count])