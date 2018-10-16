delimiter = "XXXXXX"
dictionary = []
scrambled_words = []  # (word: str, unscrambled: array)

# get user inputs
is_lower = True
min_length = 0
max_length = 0
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

    dictionary.append(user_input)

# get list of scrambled words
list_of_scrambled_words = []
min_length = 1
max_length = 6
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

    list_of_scrambled_words.append(user_input)

# output
for word in list_of_scrambled_words:
    word_filter = sorted(word)  # array of letters
    word_filter_length = len(word_filter)
    data = dictionary
    _dictionary = [word for word in data if len(word) >= word_filter_length]
    scrambled_words = []  # (word: str, unscrambled: array)

    search_result = []
    word_filter = "".join(word_filter)  # array of letters into a single word
    for dictionary_word in _dictionary:
        sorted_dictionary_word = sorted(dictionary_word)  # sorted array of letters
        sorted_dictionary_word = "".join(sorted_dictionary_word)  #  into a single word
        # print(word_filter == sorted_dictionary_word)
        if word_filter == sorted_dictionary_word:
            search_result.append(dictionary_word)

    scrambled_word = (
        word,
        search_result
    )
    scrambled_words.append(scrambled_word)

    # print results
    end_of_result_string = "******"
    for word_tuple in scrambled_words:
        unscrambled_words = word_tuple[1]
        unscrambled_words = sorted(unscrambled_words)
        if len(unscrambled_words) < 1:
            print('NOT A VALID WORD')
        else:
            for word in unscrambled_words:
                print(word)

        print(end_of_result_string)
