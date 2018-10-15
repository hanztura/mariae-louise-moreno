# from sys import stdin, stdout
from collections import Counter


# get test cases
multiplier = 1
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)

# output

output = []
for test_case in input_test_cases:
    test_case = int(test_case)

    # prime_factors = get_prime_factors(test_case)  # array of prime factors
    # https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    # get prime factores
    prime_factors = []
    i = 2
    factors = []
    n = test_case
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    factors.sort()
    prime_factors = factors

    # canonical_prime_factorization
    canonical_prime_factorization = ''
    counter = Counter(prime_factors)
    counter = dict(counter)

    for P in sorted(counter):
        a = counter[P]
        string = '({}^{})'.format(P, a)  # (P^a)
        canonical_prime_factorization += string

    print(canonical_prime_factorization)
    output.append(canonical_prime_factorization)
