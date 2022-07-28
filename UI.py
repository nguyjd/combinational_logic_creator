from tkinter import *
from tkinter import ttk
from pygubu.widgets.scrolledframe import ScrolledFrame
import pathlib
from tkinter.messagebox import showinfo

# Constants for the window
BG_COLOR = '#1E1E1E'
WIG_COLOR = '#878787'
BUTTON_COLOR = '#1E1E1E'
TEXT_COLOR = '#FFFFFF'

gui_events = []
active_signals = []
logic_list = []
selected_signal = None
have_loaded = False

def load_event(status_text, logo, circuit, opcodes_list, names_list, response):

    # Inform the user that the file is loading.
    status_text.config(text = 'Loading text file')

    # Remove all the stuff the window.
    # This is needed if the user pressed the button twice or more.
    for widgets in circuit.winfo_children():
        widgets.destroy()

    # Tell the main loop that we need information from the files.
    gui_events.append('load')

    # Create the scrolled frames
    opcodes = ScrolledFrame(circuit, scrolltype="both")

    choose_signal = ttk.Label(circuit, text = 'Choose what signal to generate.')
    global selected_signal
    selected_signal = StringVar()
    signal_cb = ttk.Combobox(circuit, textvariable=selected_signal)
    temp = []
    for name in names_list:
        temp.append(name)
    signal_cb['values'] = temp
    signal_cb['state'] = 'readonly'

    # Wait until the main loop is done loading the files
    while True:
        if len(response) != 0:
            if response.pop() == 'done':
                break
    
    # Check for error in file loading.
    if opcodes_list[0] == 'empty':
        status_text.config(text = 'opcodes.txt is a empty file')
        return
    elif opcodes_list[0] == 'badvalues':
        status_text.config(text = 'opcodes.txt contains invalid entries')
        return
    elif opcodes_list[0] == 'nofile':
        status_text.config(text = 'opcodes.txt does not exist')
        return
    if names_list[0] == 'empty':
        status_text.config(text = 'signal_names.txt is a empty file')
        return
    elif names_list[0] == 'badvalues':
        status_text.config(text = 'signal_names.txt contains invalid entries')
        return
    elif names_list[0] == 'nofile':
        status_text.config(text = 'signal_names.txt contains invalid entries')
        return
    
    # Unload the logo.
    logo.pack_forget()

    # Display the opcodes. 
    opcode_frames = ttk.Frame(opcodes.innerframe)
    ttk.Label(opcode_frames, text = 'OPCODES').pack(anchor='ne', side=TOP)
    for opcode_label in opcodes_list:
        txt = ttk.Label(opcode_frames, text = opcode_label)
        txt.pack(anchor='e', side=TOP, ipadx=14, ipady=1)
    opcode_frames.pack(anchor='n', side=LEFT)
    
    # Display all the signals with the checkboxes
    # Clear the active signals list
    global active_signals
    active_signals[:] = []
    for signal in names_list:
        signal_frame = ttk.Frame(opcodes.innerframe)
        ttk.Label(signal_frame, text = f'{signal}',justify=LEFT).pack(anchor='w', side=TOP, ipadx=0, ipady=0)
        checkbox_vars = []
        for opcode_label in opcodes_list:
            var = StringVar()
            var.set('0')
            checkbutton = ttk.Checkbutton(signal_frame)
            checkbutton.configure(
            offvalue='0',
            onvalue='1',
            text="Active",
            variable=var,
            )
            checkbutton.pack(anchor='ne', side=TOP)
            checkbox_vars.append(var)
            

        active_signals.append(checkbox_vars)
        signal_frame.pack(anchor='n', side=LEFT)

    
    # Pack the widgets and display them on the screen.
    choose_signal.pack(anchor = 'w', side=TOP, ipadx=0, ipady=0, padx=0, pady=0)
    signal_cb.pack(anchor = 'w', side=TOP, ipadx=0, ipady=0, padx=0, pady=0)
    opcodes.pack(anchor = 'n', side=LEFT, ipadx=150 ,ipady=200, padx=0, pady=0)

    # Tell the user that the loading is done.
    status_text.config(text = 'Done')

    # Save the state that we have loaded the information
    global have_loaded
    have_loaded = True

    

def Generate_event(status_text, response, names_list):

    if have_loaded: 

        # Find the signal to send
        found_signal = False
        for index, signal in enumerate(names_list):
            
            if signal.strip() == selected_signal.get().strip():
                found_signal = True

                temp = ''
                for value in active_signals[index]:
                    temp += value.get()

                logic_list.append(temp)
                gui_events.append('generate')
                status_text.config(text = 'Generating Logic')
                break
        
        if not found_signal:
            status_text.config(text = 'A signal is not selected.')
            return
        else:
            # Wait until the main loop is done generating logic
            while True:
                if len(response) != 0:
                    if response.pop() == 'done':
                        break

            showinfo(title='Successful', message='The boolean equation has been copied to the clipboard.')

        status_text.config(text = 'Done')

    else:
        status_text.config(text = 'Cannot logic as no data has been loaded.')


def CreateWindow(event_list, opcodes_list, names_list, response, logic):

    # Location of the UI file
    file_loc = str(pathlib.Path(__file__).parent.resolve())

    # Create the root object for the window.
    root = Tk()
    root.title('Combination Logic Creator')
    root.resizable(False, False)
    root.iconbitmap(f'{file_loc}/icons/LOGO.ico')
    
    # Set the threaded list in the global vars.
    global gui_events
    gui_events = event_list
    global logic_list
    logic_list = logic

    # Configure the colors of the window
    root.configure(bg = BG_COLOR)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TLabel', background = BG_COLOR, foreground = TEXT_COLOR)
    style.configure('TCheckbutton', background = WIG_COLOR, foreground = '#000000')
    style.configure('TCombobox', background = WIG_COLOR, foreground = TEXT_COLOR)
    style.configure('TFrame', background = BG_COLOR, foreground = TEXT_COLOR)
    style.configure('TButton', background = BUTTON_COLOR, foreground = TEXT_COLOR, borderwidth = 2, relief="groove")
    style.map('TButton', background=[('active', BUTTON_COLOR)])

    # Load the images.
    load_icon = PhotoImage(file = f'{file_loc}/icons/load.png')
    quit_icon = PhotoImage(file = f'{file_loc}/icons/quit.png')
    generate_icon = PhotoImage(file = f'{file_loc}/icons/generate.png')
    logo_image = PhotoImage(file = f'{file_loc}/icons/start_screen.png')

    # Create the logo of the program
    logo = ttk.Label(root, image = logo_image, borderwidth = 5)
    logo.pack()

    # A frame to hold the information.
    circuit = ttk.Frame(root)
    circuit.pack(side=TOP)

    # Frame to hold the infomation at the bottom.
    bottom_frame = ttk.Frame(root)
    bottom_frame.pack(side=BOTTOM)

    # A frame to hold the bottom.
    button_frame = ttk.Frame(root)
    button_frame.pack(anchor = 's', side=RIGHT)

    # Create a text of the status of the program
    status_text = ttk.Label(root, text = 'Done')
    status_text.pack(anchor = 's', side=LEFT)

    # Button that generate the expression.
    generate_button = ttk.Button(button_frame, image = generate_icon, command = lambda: Generate_event(status_text, response, names_list))
    generate_button.grid(column = 1, row = 0, sticky = 'se', padx = 0, pady = 0)

    # Button to load the txt files.
    load_button = ttk.Button(button_frame, image = load_icon, command = lambda: load_event(status_text, logo, circuit, opcodes_list, names_list, response))
    load_button.grid(column = 2, row = 0, sticky = 'se', ipady = 1, ipadx = 10)

    # Handle closing the window.
    quit_button = ttk.Button(button_frame, image = quit_icon, command = lambda: event_list.append('quit'))
    quit_button.grid(column = 3, row = 0, sticky = 'se', ipady = 1, ipadx = 10)
    root.protocol('WM_DELETE_WINDOW', lambda: event_list.append('quit'))

    # Start the main loop for the GUI
    root.mainloop()