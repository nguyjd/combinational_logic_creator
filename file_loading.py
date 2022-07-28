import pathlib

def load_opcodes_and_names(debug = False):

    file_loc = str(pathlib.Path(__file__).parent.resolve())
    try:
        opcodes_len = 0
        with open(file_loc + '\opcodes.txt', 'r') as file:
            opcodes = file.readlines()

        if len(opcodes) == 0:
            opcodes_empty = True
            raise ValueError('opcodes.txt is a empty file')
        else:
            opcodes_empty = False

        opcodes_len = len(opcodes[0].strip())
        print(f'opcode length: {opcodes_len}')
        for index, opcode in enumerate(opcodes):
            
            # Remove the newline
            opcodes[index] = opcode.strip()
            
            if opcodes_len != len(opcodes[index]):
                raise ValueError(f'Differing length opcodes in the opcodes.txt found on line {index + 1}')

            if len(opcodes[index]) == 0:
                raise ValueError(f'Invaild opcode in the opcodes.txt on line {index + 1}')

            # Parse the opcode.
            for char in opcodes[index]:
                if char != '1' and char != '0':
                    raise ValueError('Invaild symbol in the opcodes.txt') 

    except ValueError as err:
        if opcodes_empty:
            opcodes = ['empty']
        else:
            opcodes = ['badvalues']
        if debug:
            print(err)

    except FileNotFoundError as err:
        opcodes = ['nofile']
        if debug:
            print(err)
            print('Ensure that the file_loading.py is in the same folder with the txt files.')

    try:
        with open(file_loc + '\signal_names.txt', 'r') as file:
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
            signal_names = ['empty']
        else:
            signal_names = ['badvalue']
        if debug:
            print(err)

    except FileNotFoundError as err:
        signal_names = ['nofile']
        if debug:
            print(err)
            print('Ensure that the file_loading.py is in the same folder with the txt files.')

    return opcodes, signal_names