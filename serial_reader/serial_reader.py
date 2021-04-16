import os
import traceback

import serial
import pywinauto as winauto
import time

import PySimpleGUI as sg
f = open("D:\\Desenvolvimento\\Python\\SerialReader2\\variables\\variables.txt", "r")
comPort = f.read()
data = ''
data_backup = ''
hasChanged = False

try:
    ser = serial.Serial(comPort, 9600, timeout=10000)
except:
    traceback.print_exc()

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
