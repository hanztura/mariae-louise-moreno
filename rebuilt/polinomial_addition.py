n = 2

# get test cases
multiplier = n
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)


transformed_input_test_cases = [input_test_cases[i:i+n] for i in range(0, len(input_test_cases), n)]

for test_case in transformed_input_test_cases:
    p1 = test_case[0].split()
    p2 = test_case[1].split()

    p1 = [int(i) for i in p1]  # transform into int
    p2 = [int(i) for i in p2]  # transform into int

    p1_degree = p1[0]
    p2_degree = p2[0]

    p1_coefficients = p1[1:]
    p2_coefficients = p2[1:]

    highest_degree = p1_degree
    if p2_degree > p1_degree:
        highest_degree = p2_degree

    # compute sum of polynomial
    p_sum_coefficients = []
    for i in range(highest_degree + 1):
        if i > p1_degree:
            p1_coefficient = 0
        else:
            p1_coefficient = p1_coefficients[i]

        if i > p2_degree:
            p2_coefficient = 0
        else:
            p2_coefficient = p2_coefficients[i]

        _sum = p1_coefficient + p2_coefficient
        p_sum_coefficients.append(_sum)

    p_sum_coefficients.reverse()

    if p_sum_coefficients[0] == 0 and highest_degree > 0:
        # if highest degree has a sum of 0 coefficient
        # and length of sum of coefficients is more than 1
        p_sum_coefficients = p_sum_coefficients[1:]
        highest_degree -= 1
    
    degrees = [i for i in range(highest_degree, -1, -1)]

    # stringify answer
    answer = ""
    for (i, coefficient) in enumerate(p_sum_coefficients):
        degree = degrees[i]

        if (coefficient == 0 and highest_degree > 0):
            continue
        else:
            sign = '+'
            if coefficient < 0:
                sign = '-'

            absolute_coefficient = abs(coefficient)

            # string representation of term
            string = '{}x^{}'.format(absolute_coefficient, degree)

            if degree < highest_degree:
                string = ' {} {}'.format(sign, string)
            else:
                if coefficient < 0:
                    string = '{}{}'.format(sign, string)

            answer += string

    print(answer)