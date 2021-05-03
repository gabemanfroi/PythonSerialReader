import os
import PySimpleGUI as sg
import importlib
import site
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
site.addsitedir(os.path.join(BASE_DIR, 'utils'))
VAR_DIR = os.path.join(BASE_DIR, 'variables', 'variables.txt')
import serial_ports
sp = serial_ports

def criaTela(windowName):
    # Define the window's contents
    layout = [[sg.Text(windowName)],
              [sg.Listbox(values=sp.serial_ports(), enable_events=True, size=(40, 20), key="-FILE LIST-")],
              [sg.Text(size=(60, 2), key='-OUTPUT-')],
              [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Window Title', layout, size=(500, 500))
    return window


window = criaTela('Tela Principal')

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Ok':
        # Output a message to the window
        comPort = values['-FILE LIST-'][0]
        os.environ['COMPORT'] = comPort
        f = open(VAR_DIR, "w")
        f.write(comPort)
        f.close()

        window['-OUTPUT-'].update('Serviço iniciado utilizando a porta de Comunicação: ' + os.environ[
            'COMPORT'] + '\nFeche esta Janela para prosseguir...')

# Finish up by removing from the screen
window.close()
