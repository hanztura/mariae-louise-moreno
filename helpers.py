import re

from collections import Counter, OrderedDict
from operator import itemgetter

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


def substituion_cipher(message, base_keys, secret_keys):
    encrypted_message = []
    for word in message:
        encrypted_word = ''
        for letter in word:
            # encrypt
            try:
                index = base_keys.index(letter)
                encrypted_letter = secret_keys[index]
            except Exception as e:
                # if letter/character is not in base keys
                encrypted_letter = letter
            finally:
                encrypted_word += encrypted_letter

        encrypted_message.append(encrypted_word)

    encrypted_message = " ".join(encrypted_message)
    return encrypted_message


def inventory_reader(string_current_number_to_read):
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

    return current_read


def write_roman_numeral(num):
    """
    https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
    """
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])


def search_words(word_filter, data):
    """
    https://stackoverflow.com/questions/38210672/filter-words-that-contain-some-letters-in-a-specific-order?rq=1
    """
    # dictionary of words with greater or equal length of filter
    dictionary = [word for word in data if len(word) >= len(word_filter)]

    # reduce dictionary by letter appearance
    dictionary2 = []
    word_filter_length = len(word_filter)
    for word in dictionary:
        save_word = True
        for letter in word_filter:
            if letter not in word:
                save_word = False
                break
        if save_word and len(word) == word_filter_length:
            dictionary2.append(word)

    filtered_words = dictionary2
    return filtered_words


def get_infinite_inputs(delimiter,
    is_lower = True,
    min_length = 0,
    max_length = 0
):
    inputs = []
    while True:
        user_input = input()
        if user_input == delimiter:
            break
        
        if is_lower:
            user_input = user_input.lower()

        # validate
        if min_length > 0:
            if len(user_input) < min_length or len(user_input) < 1:
                continue

        if max_length > 0:
            if len(user_input) > max_length:
                continue
        # end validate

        inputs.append(user_input)

    return inputs
