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
    expression = "".join(expression.split())

    if debug:
        print(f'Parsing: {expression}')
        print('Parsing expression for parenthesis')

    # Find pairs of parenthesis in the string
    try:

        completedParenthesesPairs = []
        pairsStack = []
        for index, symb in enumerate(expression):

            if debug:
                print(f'Index: {index}, Symbol: {symb}')
            
            if symb == '(':
                # Create a new parenthesis pair
                pairsStack.append([index, None])

                if debug:
                    print(f'Found a Right Parentheses at index {index}')

            if symb == ')':
                # Check to see if there is a pair for the left parentheses to match with.
                if len(pairsStack) == 0:
                    raise ValueError

                # Add the index to the pair list
                completedPair = pairsStack.pop()
                completedPair[1] = index
                completedParenthesesPairs.append(completedPair)

                if debug:
                    print(f'Found a Left Parentheses at index {index}')

        # Check to see if all the parentheses have a pair
        if len(pairsStack) != 0:
            raise ValueError

        if debug:
            for pair in completedParenthesesPairs:
                print(pair)

    except ValueError:
        if debug:
            print("The expression has mismatched parentheses")
        return None

    except Exception as err:
        if debug:
            print("Exception thrown while parsing the expression")
            print(err)
        return None

    return completedParenthesesPairs

