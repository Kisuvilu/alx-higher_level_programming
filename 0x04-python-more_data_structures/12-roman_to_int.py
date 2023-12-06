#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is a string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define a dictionary to store the values of Roman numerals
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    # Iterate through the Roman string in reverse order
    for numeral in reversed(roman_string):
        # Get the value of the current numeral
        value = roman_numerals[numeral]

        # If the current numeral is smaller than the previous numeral, subtract its value
        if value < prev_value:
            total -= value
        # Otherwise, add its value to the total
        else:
            total += value

        # Update the previous value for the next iteration
        prev_value = value

    return total
