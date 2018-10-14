from collections import Counter


def get_longest_word(test_case):
    if test_case:
        longest_word = ''
        # transform test_case into an array of words
        words = test_case.split()

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        return longest_word

    return ''


def get_prime_factors(n):
    """
    https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    factors.sort()
    return factors


def get_input_test_cases(multiplier=1):

    number_of_test_cases = int(input()) * multiplier

    # get test cases
    input_test_cases = []
    for i in range(number_of_test_cases):
        test_case = input()
        input_test_cases.append(test_case)

    return input_test_cases


def get_canonical_prime_factorization(prime_factors):
    counter = Counter(prime_factors)
    counter = dict(counter)

    canonical_prime_factorization = ""  # return value
    for P in sorted(counter):
        a = counter[P]
        string = '({}^{})'.format(P, a)  # (P^a)
        canonical_prime_factorization += string

    return canonical_prime_factorization


def compute_continued_fraction(values):
    value = values[0]
    if len(values) == 1:
        fraction = 1 / value
        return fraction

    answer = (1 / (value + compute_continued_fraction(values[1:])))
    return answer


def data_counter(data):
    counter = Counter(data)
    counter = dict(counter)

    return counter
