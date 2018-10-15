
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
# get longest word of each test case
for test_case in input_test_cases:

    # get longest word
    longest_word = ''
    if test_case:
        # transform test_case into an array of words
        words = test_case.split()

        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

    answer = longest_word
    print(answer)
    output.append(longest_word)