from numeral import numeralToInt, integerToRoman, f_expression
import sys

def main():
    
    '''Checks if there are fewer than 2 elements which means that no expression was provided by the user '''
    if len(sys.argv) < 2:
        print("I don’t know how to read this.")
        return

    '''Constructing the Expression into a String'''
    expression = " ".join(sys.argv[1:])
    
    '''Handle single Roman numeral input'''
    if all(c in "IVXLCDM" for c in expression) and not any(op in expression for op in "+-*/()[]"):
        try:
            print(numeralToInt(expression))
        except Exception:
            print("I don't know how to read this.")
        return
    
    '''Evaluate the expression'''
    try:
        result = f_expression(expression)
    except Exception:
        print("I don’t know how to read this.")
        return


    '''The result conditions'''
    if result is None:
        print("I don’t know how to read this.")
        return
    if result < 0:
        print("Negative numbers can’t be represented in Roman numerals.")
    elif result == 0:
        print("0 does not exist in Roman numerals.")
    elif isinstance(result, float):
        print("There is no concept of a fractional number in Roman numerals.")
    elif result > 3999:
        print("You’re going to need a bigger calculator.")
    else:
        print(integerToRoman(result))

'''Run the program when called '''
if __name__ == "__main__":
    main()




