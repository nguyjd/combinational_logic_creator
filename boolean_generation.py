def boolean_generation(opcodes: list, actives: str, debug = False):
    # support up to 64 bits
    vars_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 's', 'x', 'y', 'z'
                    'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'as', 'ax', 'ay', 'az'
                    'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl']
    
    try:
        
        if debug:
            print(f'Opcode list: {opcodes}')
            print(f'Active signal string: {actives}')

        if len(opcodes) == 0:
            raise Exception('The opcodes list was empty')
        
        # Check if the length all the input
        for index, opcode in enumerate(opcodes):
            if len(opcode) == 0:
                raise Exception(f'At index {index}, The opcode was empty')

            if len(opcode) > len(vars_labels):
                raise Exception('Unable to handle that amount of bits')
        
        # Check if the length of input and active signals are the same
        if len(opcodes) != len(actives):
            raise Exception('Length mismatch between opcodes and active signals amount.')
        
        sop_expression = ''
        for active_index, input in enumerate(opcodes):
            
            # Check to see if the signal is active for the logic
            if actives[active_index] == '1':
                expression = ''
                for index, bit in enumerate(input):
                    if bit == '1':
                        expression += f'{vars_labels[index]}&'
                    else:
                        expression += f'~{vars_labels[index]}&'
                
                sop_expression += f'{expression[0:len(expression)-1]}+'
            
        # Remove the last or off the sop expression
        sop_expression = sop_expression[0:len(sop_expression)-1]

        if debug:
            print(f'Generated equation: {sop_expression}')

        return sop_expression

    except Exception as err:
        if debug:
                print(f'Exception thrown while generating the expression. Error Message: {err}')
        return None