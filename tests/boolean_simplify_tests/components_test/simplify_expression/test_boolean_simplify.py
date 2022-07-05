# Boolean rules
# Rules taken from https://sandbox.mc.edu/~bennet/cs110/boolalg/rules.html

# The Idempotent Laws       AA = A                      A+A = A
# The Associative Laws      (AB)C = A(BC)               (A+B)+C = A+(B+C)
# The Commutative Laws      AB = BA                     A+B = B+A
# The Distributive Laws     A(B+C) = AB+AC              A+BC = (A+B)(A+C)
# The Identity Laws         AF = F                      AT = A                  A+F = A             A+T = T
# The Complement Laws       Anot(A) = F                 A+not(A) = T            not(F) = T          not(T) = F
# The Involution Law        not(not(A)) = A
# DeMorgan's Law            not(AB) = not(A)+not(B)     not(A+B) = not(A)not(B)

def boolean_simplfy(expression: str, debug = False):

    # Remove the whitespace if there are any.
    expression = ''.join(expression.split())

    if debug:
        print(f'Parsing: {expression}')

    # Parse the string.
    completedParenthesesPairs = []
    pairsStack = []
    try:

        for index, symb in enumerate(expression):

            if debug:
                print(f'Looking at Index: {index}, Symbol: {symb}')
            
            ##---------------- Parentheses Validation ----------------------##
            if symb == '(':
                # Create a new parenthesis pair
                pairsStack.append([index, None])

                if debug:
                    print(f'Found a Right Parentheses at index {index}')

            if symb == ')':
                
                # Check to see if there is a pair for the left parentheses to match with.
                if len(pairsStack) == 0:
                    raise ValueError('Mismatch Parentheses')

                # Add the index to the pair list
                completedPair = pairsStack.pop()
                completedPair[1] = index
                completedParenthesesPairs.append(completedPair)

                if debug:
                    print(f'Found a Left Parentheses at index {index}')
            ##---------------- End of Parentheses Validation ---------------##

            ##--------------------- Symbol Validation ----------------------##
            # Check + and *. 
            if symb == '+' or symb == '*':
                
                if debug:
                    print(f'Found {symb} at index {index}')

                # Cannot have a logical symbol at the front (except !) or back.
                if index == 0 or index == (len(expression) - 1):
                    raise ValueError(f'Misplaced Logical Symbol. Index: {index}, Symbol: {symb}')

                # Check in front of the symbol
                if expression[index + 1] == '+' or expression[index + 1] == '*' or expression[index + 1] == ')':
                    raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index + 1}, Symbol: {expression[index + 1]}')

                # Check behind the symbol. NOTE: This should not be reach if the expression is invaild. Maybe remove but the behavior is not fully defined without it.
                if expression[index - 1] == '+' or expression[index - 1] == '*' or expression[index - 1] == '(':
                    raise ValueError(f'Logical symbol next to a invaild symbol. Index: {index}, Symbol: {symb} next to Index: {index - 1}, Symbol: {expression[index - 1]}')

                # Check what symbol ! is attached to.
                if expression[index + 1] == '!':
                    # check to see if we can go one more.
                    if (index + 2) < (len(expression) - 1):
                        if expression[index + 2] == '+' or expression[index + 2] == '*':
                            raise ValueError(f'Special case error. Index: {index}, Symbol: {symb} next to Index: {index + 1}, Symbol: {expression[index + 1]} next to Index: {index + 2}, Symbol: {expression[index + 2]}')

            # Check !.
            if symb == '!':
                
                if debug:
                    print(f'Found {symb} at index {index}')

                # Cannot have a logical symbol at the front or back.
                if index == (len(expression) - 1):
                    raise ValueError(f'Misplaced Logical Symbol. Index: {index}, Symbol: {symb}')
                
            ##----------------- End of Symbol Validation ----------------------##

        # Check to see if all the parentheses have a pair
        if len(pairsStack) != 0:
            raise ValueError('Mismatch Parentheses')

        if debug:
            for pair in completedParenthesesPairs:
                print(f'Found Parenthese Pair: {pair}')

    except ValueError as err:
        if debug:
            print(f'The expression is invalid. Error Message: {err}')
        return None

    except Exception as err:
        if debug:
            print(f'Exception thrown while parsing the expression. Error Message: {err}')
        return None

    # Convert the string into a list
    expression_list = []
    expression_list[:0] = expression

    # Completed verification of the string at this point.
    # Main loop to simplify
    try:
        
        for index, symb in enumerate(expression_list):

            # Idempotent - Currently O(n^2)
            if symb != '+' and symb != '*' and symb != '!' and symb != '(' and symb != ')':
                
                lookahead = index + 1
                while lookahead < len(expression_list):
                    if expression_list[lookahead] == '+':
                        break
                    
                    if symb == expression_list[lookahead]:
                        del expression_list[lookahead]
                    else:
                        lookahead += 1


    except Exception as err:
        if debug:
            print(f'Exception thrown while parsing the expression. Error Message: {err}')
        return None

    # Convert the list back into a string
    expression = ""
    for symb in expression_list:
        expression += symb

    return expression

