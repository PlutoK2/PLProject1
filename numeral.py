import sys
import re


'''Maximum allowed value'''
MAX_ROMAN_VALUE = 3999

'''Roman numeral to integer conversion'''
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

    ''''''
    f_total = 0
    prev_value = 0
    '''Process the string in reverse order'''
    for char in reversed(numeral):
        value = ROMAN_NUM.get(char, 0)
        ''' indicates that the numeral should be subtracted from the total '''
        if value < prev_value:
            f_total -= value
        else:
            f_total += value
    prev_value = value
    '''function returns the total integer value calculated from the Roman numeral.'''
    return f_total

'''integer to roman numeral conversion'''
def integerToRoman(num: int) -> str:
    if num <= 0:
        return "0 does not exist in Roman numerals."
    if num > MAX_ROMAN_VALUE:
        return "You’re going to need a bigger calculator."

    val = [1000, 900, 500, 400,100, 90, 50, 40,10,9, 5, 4,1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

    roman_numeral = ""
    '''for loop checks if the current integer num is greater than or equal to the current value'''
    for i in range(len(val)):
        while num >= val[i]: 
            roman_numeral += syms[i]
            num -= val[i]
    '''returns the complete roman_numeral string'''
    return roman_numeral 

'''Evaluates mathematical expression containing Roman numerals and returns the result as an integer.'''
def f_expression(expression: str) -> int:

    try:
        '''Replace Roman numerals with integers for evaluation'''
        keys = expression.split()
        for i in range(len(keys)):
                if all(c in "IVXLCDM" for c in keys[i]):
                    keys[i] = str(numeralToInt(keys[i]))
            
        '''Create a new expression from integer keys'''
        f_expr = " ".join(keys)
        '''Evaluate the expression'''
        result = eval(f_expr) 
        return result

    except (ZeroDivisionError, SyntaxError, ValueError):
        return None


'''Testing the functions'''
if __name__ == "__main__":
    print(numeralToInt("XIV"))  # Output: 14
    print(numeralToInt("MCMXCIV"))  # Output: 1994
    print(numeralToInt("MMXXIV"))  # Output: 2024

    print(integerToRoman(14))  # Output: XIV
    print(integerToRoman(1994))  # Output: MCMXCIV
    print(integerToRoman(2024))  # Output: MMXXIV











    