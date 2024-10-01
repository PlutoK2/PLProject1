from conversion import numeral

def test_numeralToIntReturnType():
    assert type(numeral.numeralToInt('I')) == int

def test_numeralToIntPartialRange():
    assert numeral.numeralToInt("V") == 5
    assert numeral.numeralToInt("IV") == 4
    assert numeral.numeralToInt("X") == 10
    assert numeral.numeralToInt("I") == 1
    assert numeral.numeralToInt("VII") == 7
    

    

 
