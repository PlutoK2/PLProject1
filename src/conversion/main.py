from numeral import numeralToInt, integerToRoman, f_expression
import sys

def main():
    '''
    This program  processes user input from the command line and evaluates it as a mathematical expression or a Roman numeral.

    Args:
        Does not take any arguments directly. It utilizes sys.argv to read command-line arguments.

    Returns:
        The function uses print statements to communicate with the user but does not return a value. '''
    
    #Checks if there are fewer than 2 elements which means that no expression was provided by the user
    if len(sys.argv) < 2:
        print("I don’t know how to read this.")
        return

    #Constructing the Expression into a String
    expression = " ".join(sys.argv[1:])
    
    #Handle single Roman numeral input
    if all(c in "IVXLCDM" for c in expression) and not any(op in expression for op in "*()[]"):
        try:
            print(numeralToInt(expression))
        except ValueError:
            print("I don't know how to read this.")
        return
    
    #Evaluate the expression
    
    result = f_expression(expression)
    


    #The result conditions
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
        print(numeralToInt(result))
        print(integerToRoman(result))

#Run the program when called
if __name__ == "__main__":
    main()




