import sys
import re


#Maximum allowed value
MAX_ROMAN_VALUE = 3999


def numeralToInt(numeral:str) -> int:
    if not is_valid_roman(numeral):
        raise ValueError(f"Invalid Roman numeral: {numeral}")
    """
    This program should take a roman numeral and return it into a integer.

    Args:
        numeral (str) : The roman numeral

    Returns:
        int: Returning the string of the roman numeral to an int 

    Raise: 
        ValueError: if value isnt a numeral
    """

    ''''''

    #Roman numeral and integer values
    ROMAN_NUM = {
   'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
}
    f_total = 0
    prev_value = 0
    
    i = len(numeral) - 1
    
    while i >= 0:
        # Check for two-character numerals first
        if i > 0 and numeral[i-1:i+1] in ROMAN_NUM:
            value = ROMAN_NUM[numeral[i-1:i+1]]
            f_total += value
            i -= 2  # Skip the next character since we processed a pair
        else:
            value = ROMAN_NUM[numeral[i]]
            if value < prev_value:
                f_total -= value
            else:
                f_total += value
            prev_value = value
            i -= 1  # Move to the next character

    return f_total

#integer to roman numeral conversion
def integerToRoman(num: int) -> str:
    """
    This program should take a integer and return it into a roman number.

    Args:
        num(int) : The integer value

    Returns:
        str: Returning the int to a string
    """

    ''''''
    if num <= 0:
        return "0 does not exist in Roman numerals."
    if num > MAX_ROMAN_VALUE:
        return "You’re going to need a bigger calculator."

    val = [1000, 900, 500, 400,100, 90, 50, 40,10,9, 5, 4,1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

    roman_numeral = ""
    #for loop checks if the current integer num is greater than or equal to the current value
    for i in range(len(val)):
        while num >= val[i]: 
            roman_numeral += syms[i]
            num -= val[i]
    #returns the complete roman_numeral string
    return roman_numeral 

def f_expression(expression: str) -> int:
    """
    This program should process a mathematical or logical expression represented as a string.

    Args:
        expression (str) : The expression

    Returns:
        int: Evaluating the expression and returning the result as an integer
    
    Raises:
        ValueError: invaild keys in an expression.
    
    """


    ''''''
   

    try:
        #Replace Roman numerals with integers for evaluation
        keys = expression.split()
        for i in range(len(keys)):
                if all(c in "IVXLCDM" for c in keys[i]):
                    keys[i] = str(numeralToInt(keys[i]))
                elif not keys[i].isdigit() and keys[i] not in "+-*/":
                    raise ValueError(f"Invalid token: {keys[i]}")
            
        #Create a new expression from integer keys
        f_expr = " ".join(keys)
        #Evaluate the expression
        result = eval(f_expr) 
        return result

    except (ZeroDivisionError, SyntaxError, ValueError):
        return None
    
def is_valid_roman(numeral: str) -> bool:
    # Regular expression to match valid Roman numeral patterns
    pattern = r"^(M{0,3})(CM|CD|D?|C{0,3})(XC|XL|L?|X{0,3})(IX|IV|V?|I{0,3})$"
    return re.match(pattern, numeral) is not None



#Testing the functions
if __name__ == "__main__":
    print(numeralToInt("XIV"))  # Output: 14
    print(numeralToInt("MCMXCIV"))  # Output: 1994
    print(numeralToInt("MMXXIV"))  # Output: 2024
    print(numeralToInt("XL")) 

    print(integerToRoman(14))  # Output: XIV
    print(integerToRoman(1994))  # Output: MCMXCIV
    print(integerToRoman(2024))  # Output: MMXXIV











    