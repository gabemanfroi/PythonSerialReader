import os
import subprocess

i = 0

subprocess.run("py -m SerialReader2.gui.gui")
subprocess.run("py -m SerialReader2.serial_reader.serial_reader")

porta = ''

def alteraCOM(value):
    porta = value

while os.getenv('COMPORT') is not None:
    print('foi')
