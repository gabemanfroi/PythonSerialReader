import os
import traceback
import serial
import pywinauto as winauto
import time

import PySimpleGUI as sg
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAR_DIR = os.path.join(BASE_DIR, 'variables', 'variables.txt')
f = open(VAR_DIR, "r")
comPort = f.read()
data = ''
data_backup = ''
hasChanged = False

ser = serial.Serial(comPort, 9600, timeout=10000)

while True:
    if (ser.inWaiting() > 0):  # if incoming bytes are waiting to be read from the serial input buffer

        data = ser.read(ser.inWaiting()).decode('ascii')
        data = data.replace('\x02', '').replace('\r', '')
        data = data[len(data) - 6: len(data)]

        if (data != data_backup and data != '00.000'):
            data_backup = data
            winauto.keyboard.send_keys('{RIGHT}')
            winauto.keyboard.send_keys('{UP}')
            winauto.keyboard.send_keys(data.replace('.', ','))
            winauto.keyboard.send_keys('{VK_RETURN}')
            winauto.keyboard.send_keys('{LEFT}')