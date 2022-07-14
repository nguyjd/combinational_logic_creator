
def load_opcodes_and_names():
    try:
        with open('opcodes.txt', 'r') as file:
            opcodes = file.readlines()

        if len(opcodes) == 0:
            opcodes_empty = True
            raise ValueError('opcodes.txt is a empty file')
        else:
            opcodes_empty = False

        for index, opcode in enumerate(opcodes):
            
            # Remove the newline
            opcodes[index] = opcode.strip()

            if len(opcodes[index]) == 0:
                raise ValueError(f'Invaild opcode in the opcodes.txt on line {index + 1}')

            # Parse the opcode.
            for char in opcodes[index]:
                if char != '1' and char != '0':
                    raise ValueError('Invaild symbol in the opcodes.txt') 

    except ValueError as err:
        if opcodes_empty:
            opcodes = 'empty'
        else:
            opcodes = 'badvalues'
        print(err)

    except FileNotFoundError as err:
        opcodes = 'nofile'
        print(err)
        print('Ensure that the program is ran in the root folder.')

    try:
        with open('signal_names.txt', 'r') as file:
            signal_names = file.readlines()

        if len(signal_names) == 0:
            signal_names_empty = True
            raise ValueError('signal_names.txt is a empty file')
        else:
            signal_names_empty = False

        # Remove the newline
        for index, name in enumerate(signal_names):
            signal_names[index] = name.strip()

            if len(signal_names[index]) == 0:
                raise ValueError(f'Invaild name in the signal_names.txt on line {index + 1}')

    except ValueError as err:
        if signal_names_empty:
            signal_names = 'empty'
        else:
            signal_names = 'badvalue'
        print(err)

    except FileNotFoundError as err:
        signal_names = 'nofile'
        print(err)
        print('Ensure that the program is ran in the root folder.')

    return opcodes, signal_names