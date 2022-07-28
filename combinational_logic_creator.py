import multiprocessing

# Project created modules
from file_loading import load_opcodes_and_names
from music_player import PlayMusic
import UI

if __name__ == '__main__':

    manager = multiprocessing.Manager()
    gui_events = manager.list()
    response_list = manager.list()
    logic_list = manager.list()
    opcodes_list = manager.list()
    signals_list = manager.list()

    # Start playing the music
    sound_process = multiprocessing.Process(target=PlayMusic)
    sound_process.start()

    # Start the window process
    window_process = multiprocessing.Process(target=UI.CreateWindow, args=(gui_events,opcodes_list,signals_list,response_list,logic_list,))
    window_process.start()

    # main loop
    while True:

        if len(gui_events) != 0:
            match gui_events.pop():
                case 'quit':
                    sound_process.terminate()
                    window_process.terminate()
                    break
                case 'load':
                    
                    # Clear the opcodes and the names
                    opcodes_list[:] = []
                    signals_list[:] = []

                    # Load the files
                    opcodes, signals = load_opcodes_and_names()
                    
                    # add the loaded names and opcodes
                    for opcode in opcodes:
                        opcodes_list.append(opcode)
                    for signal in signals:
                        signals_list.append(signal)

                    # Tell the UI that the program is done.
                    response_list.append('done')

                case 'generate':
                    
                    while len(logic_list) == 0:
                        pass
                    
                    print('----------------------------------------------------------------------------------')
                    print('Requested generation')
                    print(logic_list.pop())
                    print('----------------------------------------------------------------------------------')

                    # Tell the UI that the program is done.
                    response_list.append('done')
                    
                    

    