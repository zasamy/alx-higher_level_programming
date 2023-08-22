#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [romans[i] for i in roman_string] + [0]
    conv = 0
    for x in range(len(numbers) - 1):
        if numbers[x] >= numbers[x+1]:
            conv += numbers[x]
        else:
            conv -= numbers[x]
    return conv
