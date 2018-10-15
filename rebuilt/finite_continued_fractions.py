# get test cases
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
    test_case = [int(x) for x in test_case]
    base = test_case[0]

    if len(test_case) > 1:

        def compute_continued_fraction(values):
            value = values[0]
            if len(values) == 1:
                fraction = 1 / value
                return fraction

            answer = (1 / (value + compute_continued_fraction(values[1:])))
            return answer

        answer = base + compute_continued_fraction(test_case[1:])

        answer = round(answer, 6)
    else:
        answer = test_case[0]

    print(answer)
