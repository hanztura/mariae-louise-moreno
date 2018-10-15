n = 2
multiplier = n
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)

base_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# first line is the message to be encrypted,
# second line is the entries in the substitution table
transformed_input_test_cases = [input_test_cases[i:i+n] for i in range(0, len(input_test_cases), n)]
for test_case in transformed_input_test_cases:
    message = test_case[0].split()
    secret_keys = test_case[1]
    secret_keys = [i for i in secret_keys]

    # encrypted_message = substituion_cipher(message, base_keys, secret_keys)
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

    print(encrypted_message)