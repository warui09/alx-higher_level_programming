#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string:
        return None
    else:
        roman_values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        length = len(roman_string)
        total = 0
        i = 0
        while i < length:
            if i + 1 < length and roman_string[i : i + 2] in (
                "IV",
                "IX",
                "XL",
                "XC",
                "CD",
                "CM",
            ):
                total += (
                    roman_values[roman_string[i + 1]] - roman_values[roman_string[i]]
                )
                i += 2
            else:
                total += roman_values[roman_string[i]]
                i += 1
        return total
