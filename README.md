# Combinational Logic Creator

This program will create boolean expression using a GUI

<b>Project Members</b>
<ul>  
  <li>Jonathon Nguyen</li>
</ul>

## How to use our project

To start using the program. Two text file are needed.
- opcodes.txt
- signal_names.txt

opcodes.txt contains the 'truth table' input portion
For example in this truth table below, appending y_i to x_i is the opcode for this program.
<p align="left" style="margin-bottom: 0px">
  <img height="300" src="https://upload.wikimedia.org/wikipedia/commons/9/90/Truth_Table_of_Half_Adder.png" alt="half adder" align="center">
</p>
<p align="left" >Figure 1: Truth table of a half adder.</p>

opcodes for the truth table.
- 00
- 01
- 10
- 11


signal_names.txt contains the names of the signal that you are trying to generate for.  
For example in this truth table above, it would be s_i and r_i+1

Once the two text files are filled out. The load text file button is clicked.  
Fill in the truth table and select a signal to be generated. Then click the generate logic button.  
That will copy the expression to your clipboard.


# Requirements

The Python version is developed on 3.10 on Windows 11.
- Python 3.10 or later
- Windows OS
- Python libraries
  - boolean.py
  - simpleaudio
  - pillow
  - pygubu
  - pyperclip

# Features

- [x] Generate boolean expressions
- [x] Simplify boolean expression
- [x] Uses a GUI
- [x] Audio player
