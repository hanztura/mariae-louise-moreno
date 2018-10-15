# For this exercise, you have to write five different computer programs. A
# submission link is available in UVLe for each program.
# • Make sure that your algorithm works given the sample input and output.
# You must also check if your algorithm can also handle input other than
# the ones given.
# • Please remove any prompt messages (e.g. Enter number: ) when getting
# input. Prompt messages will mess with your output, making your
# solution invalid.
# • See the sample input and output to guide you on what and how your
# program must display output.
# • Submit your solutions on or before Sunday, September 23 at 11:59pm.
from helpers import *


def longest_word():
    """
    Write a program that prints the longest word among a given a sequence of
    words.

    Input
    Input will start with the number of test cases t, followed be t test cases. Each
    test case t is a line consisting of one or more words, delimited by a space.

    Output
    For each test case, output the longest word. If there are ties, output the first
    longest word from the left.
    """

    # get test cases
    input_test_cases = get_input_test_cases()

    # output

    output = []
    # get longest word of each test case
    for test_case in input_test_cases:
        longest_word = get_longest_word(test_case)

        print(longest_word)
        output.append(longest_word)


def canonical_prime_factorization():
    """
    Input
    Input will start with the number of test cases t, followed by t test cases. Each
    test case is a natural number N such that 2 ≤ N ≤ 1000000.

    Output the canonical prime factorization of N. Print ‘(p^a)’ for each prime
    power p
    a
    in the factorization. The output for each test case must start in a new
    line
    """

    # get test cases
    input_test_cases = get_input_test_cases()

    # output

    output = []
    for test_case in input_test_cases:
        test_case = int(test_case)
        prime_factors = get_prime_factors(test_case)  # array of prime factors
        canonical_prime_factorization = get_canonical_prime_factorization(prime_factors)

        print(canonical_prime_factorization)
        output.append(canonical_prime_factorization)


def polinomial_addition():
    """
    Given two polynomials, P(x) of degree n and Q(x) of degree m, the sum P(x)+
    Q(x) is computed by adding the like terms. For example, for polynomials
    P(x) = x
    7 + 4x
    3 + 3x + 1
    Q(x) = 3x
    5 + 6x
    3 + x + 20
    the sum P(x) + Q(x) is equal to
    (1 + 0)x
    7 + (0 + 3)x
    5 + (4 + 6)x
    3 + (3 + 1)x + (1 + 20)
    which can then be simplified to
    x
    7 + 3x
    5 + 10x
    3 + 4x + 21
    Write a program that computes the sum of two polynomials,
    P(x) = amx
    m + am−1x
    m−1 + . . . + a2x
    2 + a1x
    1 + a0x
    0
    Q(x) = bnx
    n + bn−1x
    n−1 + . . . + b2x
    2 + b1x
    1 + b0x
    0
    given their degrees m, n and the coefficients a0, a1, . . . am−1, am and
    b0, b1, . . . bn−1, bm. Assume that m, n ≥ 0 and n is not always equal to m
    """
    n = 2
    input_test_cases = get_input_test_cases(n)
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

def finite_continued_fractions():
    input_test_cases = get_input_test_cases()

    for test_case in input_test_cases:
        test_case = test_case.split()
        test_case = [int(x) for x in test_case]
        base = test_case[0]

        if len(test_case) > 1:
            answer = base + compute_continued_fraction(test_case[1:])
            answer = round(answer, 6)
        else:
            answer = test_case[0]

        print(answer)


def histogram():
    n = 2
    input_test_cases = get_input_test_cases(n)

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

        counted_data = data_counter(data)

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
