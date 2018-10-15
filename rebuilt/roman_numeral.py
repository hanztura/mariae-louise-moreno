from collections import OrderedDict

multiplier = 1
number_of_test_cases = int(input()) * multiplier

# get test cases
input_test_cases = []
for i in range(number_of_test_cases):
    test_case = input()
    input_test_cases.append(test_case)


for test_case in input_test_cases:
    test_case = int(test_case)
    if test_case < 1 or test_case > 3999:
        print('Invalid Input')
        continue
    else:
        # answer = write_roman_numeral(test_case)
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

        answer = "".join([a for a in roman_num(test_case)])
        print(answer)