from conversion import numeral


def test_numeralToIntReturnType():
    assert type(numeral.numeralToInt('I')) == int

def test_numeralToIntPartialRange():
    assert numeral.numeralToInt("V") == 5
    assert numeral.numeralToInt("IV") == 4
    assert numeral.numeralToInt("X") == 10
    assert numeral.numeralToInt("I") == 1
    assert numeral.numeralToInt("VII") == 7

def test_integerToRoman():
    assert numeral.integerToRoman(1) == "I"
    assert numeral.integerToRoman(4) == "IV"
    assert numeral.integerToRoman(5) == "V"
    assert numeral.integerToRoman(10) == "X"
    assert numeral.integerToRoman(3999) == "MMMCMXCIX"
    assert numeral.integerToRoman(0) == "0 does not exist in Roman numerals."
    assert numeral.integerToRoman(4000) == "You’re going to need a bigger calculator."

def test_numeralToIntEdgeCases():
    assert numeral.numeralToInt("MMM") == 3000  # Check largest valid numeral
    assert numeral.numeralToInt("MMMCMXCIX") == 3888  # Check large valid numeral

def test_MixedInput():
    assert numeral.numeralToInt("XIIIa") == "I don’t know how to read this"  # Mixed valid and invalid
    assert numeral.numeralToInt("4000") ==   "Youre going to need a bigger calculator"

def test_f_expression():
    assert numeral.f_expression("IV - I") == 3
    assert numeral.f_expression("X / 0") is None  # Division by zero
    assert numeral.f_expression("X + IV *") is None  # Invalid expression

def test_VaildRoman():
    assert numeral.VaildRoman("IIII") == "I don’t know how to read this"
    

    

 
