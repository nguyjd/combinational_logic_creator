import boolean

def boolean_simplfy(expression: str, debug = False):

    # Remove the whitespace if there are any.
    expression = ''.join(expression.split())

    if debug:
        print(f'Parsing: {expression}')

    # Parse the string.
    try:

        if len(expression) == 0:
            raise ValueError('Empty expression')

        unaccountedPair = 0
        for index, symb in enumerate(expression):

            if debug:
                print(f'Looking at Index: {index}, Symbol: {symb}')
            
            ##---------------- Parentheses Validation ----------------------##
            if symb == '(':
                unaccountedPair += 1

                if index - 1 >= 0:
                    if expression[index - 1] != '!' and expression[index - 1] != '*'    \
                    and expression[index - 1] != '&' and expression[index - 1] != '|'   \
                    and expression[index - 1] != '+' and expression[index - 1] != '~':
                        raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index - 1}, Symbol: {expression[index - 1]}')

                if debug:
                    print(f'Found a Right Parentheses at index {index}')

            elif symb == ')':
                
                if len(expression) > index + 1:
                    if expression[index + 1] != '!' and expression[index + 1] != '*'    \
                    and expression[index + 1] != '&' and expression[index + 1] != '|'   \
                    and expression[index + 1] != '+' and expression[index + 1] != '~':
                        raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index + 1}, Symbol: {expression[index + 1]}')

                # Check to see if there is a pair for the left parentheses to match with.
                if unaccountedPair == 0:
                    raise ValueError('Mismatch Parentheses')

                unaccountedPair -= 1

                if debug:
                    print(f'Found a Left Parentheses at index {index}')
            ##---------------- End of Parentheses Validation ---------------##

            ##--------------------- Symbol Validation ----------------------##
            # Check | and &. 
            elif symb == '|' or symb == '&':
                
                if debug:
                    print(f'Found {symb} at index {index}')

                # Cannot have a logical symbol at the front (except ~) or back.
                if index == 0 or index == (len(expression) - 1):
                    raise ValueError(f'Misplaced Logical Symbol. Index: {index}, Symbol: {symb}')

                # Check in front of the symbol
                if expression[index + 1] == '|' or expression[index + 1] == '&'     \
                    or expression[index + 1] == ')' or expression[index + 1] == '*' \
                    or expression[index + 1] == '+' or expression[index + 1] == '!':
                    raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index + 1}, Symbol: {expression[index + 1]}')

                # Check behind the symbol. NOTE: This should not be reach if the expression is invaild. Maybe remove but the behavior is not fully defined without it.
                if expression[index - 1] == '|' or expression[index - 1] == '&'     \
                    or expression[index - 1] == '(' or expression[index - 1] == '~' \
                    or expression[index - 1] == '+' or expression[index - 1] == '!' \
                    or expression[index - 1] == '*':
                    raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index - 1}, Symbol: {expression[index - 1]}')

            # Check ~.
            elif symb == '~' or symb == '!':
                
                if debug:
                    print(f'Found {symb} at index {index}')

                # Cannot have a logical symbol in the back.
                if index == (len(expression) - 1):
                    raise ValueError(f'Misplaced Logical Symbol. Index: {index}, Symbol: {symb}')

            ##----------------- End of Symbol Validation ----------------------##

        # Check to see if all the parentheses have a pair
        if unaccountedPair != 0:
            raise ValueError('Mismatch Parentheses')

    except ValueError as err:
        if debug:
            print(f'The expression is invalid. Error Message: {err}')
        return None

    except Exception as err:
        if debug:
            print(f'Exception thrown while parsing the expression. Error Message: {err}')
        return None

    # Simplify the expression
    try:
        algebra = boolean.BooleanAlgebra()
        expression = str(algebra.parse(expression).simplify())
    except Exception as err:
        if debug:
            print(f'Exception thrown while simplifying the expression. Error Message: {err}')
        return None
    
    return expression

