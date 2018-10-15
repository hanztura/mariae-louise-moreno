
delimiter = "XXXXXX"
dictionary = []
scrambled_words = []  # (word: str, unscrambled: array)

# get user inputs
# dictionary = get_infinite_inputs(delimiter)
dictionary = []
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


# list_of_scrambled_words = get_infinite_inputs(delimiter, min_length=1, max_length=6)
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


for word in list_of_scrambled_words:
    # search_result = sorted(search_words(word, dictionary))
    word_filter = word
    data = dictionary
    _dictionary = [word for word in data if len(word) >= len(word_filter)]
    scrambled_words = []  # (word: str, unscrambled: array)

    # reduce dictionary by letter appearance
    dictionary2 = []
    word_filter_length = len(word_filter)
    for word in _dictionary:
        save_word = True
        for letter in word_filter:
            if letter not in word:
                save_word = False
                break
        if save_word and len(word) == word_filter_length:
            dictionary2.append(word)

    search_result = dictionary2

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