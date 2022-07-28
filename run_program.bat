echo off
pip install -r ./requirements.txt
echo DO NOT CLOSE THE PROGRAM THROUGH THE CONSOLE. DO NOT CLICK THE X ON THE CONSOLE
timeout /t 5
python3 ./combinational_logic_creator.py