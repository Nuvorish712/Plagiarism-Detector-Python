from tkinter import font
from Code import *
from subprocess import run
from tkinter.constants import TRUE
import PySimpleGUI as sg

fnt = 'Arial 44'

file_list_column = [
    [
        sg.In(size=(50, 1), enable_events=True, key="File1", default_text='Please choose File 1', font='fnt'),
        sg.FileBrowse(key='f1', font='fnt'),
    ],
    [
        sg.In(size=(50, 1), enable_events=True, key="File2", default_text='Please choose File 2', font='fnt'),
        sg.FileBrowse(key = 'f2', font='fnt'),
    ],
]
layout = [
    [sg.Column(file_list_column)],
    [sg.Button('Check Simmilarities', key=('exe'), font='fnt')],
    [sg.Output(size =(50, 5), key=('Output'), font='fnt')],
    [
        sg.Button('Clear', key=('clear'), font='fnt'),
        sg.Button('Exit', key=('exit'), font='fnt')
    ]
]
window = sg.Window("Plagiarism Detector", layout, size=(800,500), resizable=(TRUE))
while True:
    event, values = window.read()
    if event == "exe":
        window.FindElement('Output').Update('')
        file1 = values['f1']
        file2 = values['f2']
        if (file1 != "" and file2 != ""):
            cmp(file1, file2)
        else:
            print("Please choose appropriate files")

    if event == "clear":
        window.FindElement('Output').Update('')

    if event == "exit" or event == sg.WIN_CLOSED:
        break
window.close()