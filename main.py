import os
import subprocess
import site
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUI_DIR = os.path.join(BASE_DIR, 'gui', 'gui.py')
SERIAL_READER_DIR = os.path.join(BASE_DIR, 'serial_reader', 'serial_reader.py')

subprocess.run("py " + GUI_DIR)
subprocess.run("py " + SERIAL_READER_DIR)

porta = ''


def alteraCOM(value):
    porta = value


while os.getenv('COMPORT') is not None:
    print('foi')
