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

    counter = Counter(test_case)
    data = dict(counter)

    sorted_data = sorted(
        data.items(),
        key=itemgetter(0))  # sort alpha
    sorted_data = sorted(
        sorted_data,
        key=itemgetter(1),
        reverse=True)  # sort by occurence
    
    # check if sorted data if equal, should be alpa sorted
    # alpha_sorted_data = []  # (letter_string: occurence_int)
    for (i, value) in enumerate(sorted_data):
        previous_index = i - 1
        next_index = i + 1
        if previous_index < 0:
            pass

    answer = ''
    for i in sorted_data:
        answer += i[0]

    print(answer)