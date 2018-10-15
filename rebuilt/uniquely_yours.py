from collections import Counter
from operator import itemgetter


multiplier = 1
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)


for test_case in input_test_cases:
    test_case = test_case.lower().replace(' ', '')
    # data = data_counter(test_case)

    # counter = Counter(test_case)
    # data = dict(counter)

    data = test_case
    unique_chars = []
    unique_chars_count = []
    for char in data:
        if char not in unique_chars:
            unique_chars.append(char)

    # count
    counter = Counter(data)
    counter = dict(counter)
    for (i, unique_char) in enumerate(unique_chars):
        count = counter[unique_char]
        unique_chars_count.append(count)

    zipped = zip(unique_chars, unique_chars_count)

    sorted_data = sorted(
        zipped,
        key=itemgetter(1),
        reverse=True)  # sort by occurence

    base_chars = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    non_alpha_chars = []
    for (i, value_tuple) in enumerate(sorted_data):
        letter = value_tuple[0]
        if letter not in base_chars:
            non_alpha_chars.append(
                (i, value_tuple)
            )
            continue

    temp_counter = 0
    for i in non_alpha_chars:  # remove non alpha char
        index = i[0]
        del sorted_data[index- temp_counter] 
        temp_counter += 1

    sorted_data = sorted(
        sorted_data,
        key=itemgetter(0))  # sort by alpha
    sorted_data = sorted(
        sorted_data,
        key=itemgetter(1),
        reverse=True)  # sort by occurence

    non_alpha_chars
    temp_sorted_data = []
    for (k, i) in enumerate(non_alpha_chars):
        # find proper index
        char = i[1][0]
        occurence = i[1][1]
        for (index, data) in enumerate(sorted_data):
            previous_index = index - 1
            next_index = index + 1
            has_next = False
            has_previous = False
            if next_index < len(sorted_data):
                has_next = True
                next_letter = sorted_data[next_index][0]
                next_occurence = sorted_data[next_index][1]

            if previous_index >= 0:
                has_previous = True

            if has_next:
                if next_occurence <= occurence:
                    temp_sorted_data.append((index, i[1]))
                    breakme1 = True
                    break
            else:
                temp_sorted_data.append((index, i[1]))
                breakme1 = True
                break

    temp_counter = 0
    for non_alpha_char in temp_sorted_data:
        temp_counter += 1
        char = non_alpha_char[1][0]
        occurence = non_alpha_char[1][1]
        index = non_alpha_char[0] + temp_counter + 1

        sorted_data.insert(index, (char, occurence))

    answer = ''
    for i in sorted_data:
        answer += i[0]

    print(answer)