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

    # Find pairs of parenthesis in the string
    for symb in expression:
        print(symb)


    # bool 
    most_simple = False

    # while not most_simple:

        


        # Implment