import sys
import re


 #Maximum allowed value
MAX_ROMAN_VALUE = 3999

#Roman numeral to integer conversion
ROMAN_NUM = {
   "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
    "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
}

def numeralToInt(numeral:str) -> int:
    """
    This program should take a roman numeral and return it into a integer.

    Args:
        numeral (str) : The roman numeral

    Returns:
        int: Returning the string of the roman numeral to an int 
    """
    
    
    pass

    f_total = 0
    prev_value = 0

    for char in reversed(numeral):
        value = ROMAN_NUM.get(char, 0)
    if value < prev_value:
        f_total -= value
    else:
        f_total += value
    prev_value = value
    
    return f_total

#integer to roman numeral conversion
def integerToRoman(num: int) -> str:
    if num <= 0:
        return "0 does not exist in Roman numerals."
    if num > 3999:
        return "You’re going to need a bigger calculator."

    val = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10,9, 5, 4,
    1
    ]
    syms = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
    ]

    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]: #loop checks if the current integer num is greater than or equal to the current value
            roman_numeral += syms[i]
            num -= val[i]
    return roman_numeral # returns the complete roman_numeral string


def f_expression(expression: str) -> int:

    try:
    
            # Replace Roman numerals with integers for evaluation
        keys = expression.split()
        for i, keys in enumerate(keys):
                if all(c in "IVXLCDM" for c in keys):
                    keys[i] = str(numeralToInt(keys))
            
            # Create a new expression from integer tokens
        f_expr = " ".join(keys)
        result = eval(f_expr)  # Evaluate the expression
        return result

    except (ZeroDivisionError, SyntaxError, ValueError):
        return None


# Testing the functions
if __name__ == "__main__":
    print(numeralToInt("XIV"))  # Output: 14
    print(numeralToInt("MCMXCIV"))  # Output: 1994
    print(numeralToInt("MMXXIV"))  # Output: 2024

    print(integerToRoman(14))  # Output: XIV
    print(integerToRoman(1994))  # Output: MCMXCIV
    print(integerToRoman(2024))  # Output: MMXXIV











    