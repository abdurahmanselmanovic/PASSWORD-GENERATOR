import PySimpleGUI as sg
import password
import pyperclip
from notifypy import Notify
sg.theme('DarkBrown4')   

notification = Notify()
notification.title = 'Password Generator'
notification.message = 'Your password has been generated'
layout = [  [sg.Checkbox('Enable numbers')],
            [sg.Checkbox('Enable symbols')],
            [sg.Text('Enter lenght'), sg.InputText()],
            [sg.Button("Generate"), sg.Cancel()]]



window = sg.Window('password generator', layout)





while True:             
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    password = (password.password_generator(values[0], values[1],int(values[2])))
    sg.popup(password)
    pyperclip.copy(password)
    notification.send()
window.close()

