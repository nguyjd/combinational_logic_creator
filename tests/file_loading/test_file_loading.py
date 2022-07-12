import glob
import os

try:
    

    for file in glob.glob("*.txt"): 
        print(file)


except FileNotFoundError:
    print("Exception thrown during moving directory. The python shell must be ran from root directory.")
