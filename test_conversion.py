from conversion import numeral

'''Checks that the return type of the numeralToInt function is int when given a valid Roman numeral.'''
def test_numeralToIntReturnType():
    assert type(numeral.numeralToInt('I')) == int
'''tests the numeralToInt function with various Roman numerals'''
def test_numeralToIntPartialRange():
    assert numeral.numeralToInt("V") == 5
    assert numeral.numeralToInt("IV") == 4
    assert numeral.numeralToInt("X") == 10
    assert numeral.numeralToInt("I") == 1
    assert numeral.numeralToInt("VII") == 7
''' tests the integerToRoman function with a variety of integers'''
def test_integerToRoman():
    assert numeral.integerToRoman(1) == "I"
    assert numeral.integerToRoman(4) == "IV"
    assert numeral.integerToRoman(5) == "V"
    assert numeral.integerToRoman(10) == "X"
    assert numeral.integerToRoman(3999) == "MMMCMXCIX"
    assert numeral.integerToRoman(0) == "0 does not exist in Roman numerals."
    assert numeral.integerToRoman(4000) == "You’re going to need a bigger calculator."
'''This function checks edge cases for the maximum valid Roman numeral values'''
def test_numeralToIntEdgeCases():
    assert numeral.numeralToInt("MMM") == 3000  # Check largest valid numeral
    assert numeral.numeralToInt("MMMDCCCLXXXVIII") == 3888  # Check large valid numeral
'''tests how numeralToInt handles mixed inputs'''
def test_numeralToIntMixedInput():
    assert numeral.numeralToInt("XIIIa") == 0  # Mixed valid and invalid
    assert numeral.numeralToInt("CIVI") == 0  # Invalid placement
    assert numeral.numeralToInt("X + V") == 0  # Expression, should return 0




    

    

 
