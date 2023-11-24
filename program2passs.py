import random
import string
import PySimpleGUI as sg

upper = random.sample(string.ascii_uppercase, 2)
lower = random.sample(string.ascii_lowercase, 3)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)
total = upper + lower + digits + symbols
total = random.sample(total, len(total))
password = ''.join(total)

sg.theme("DarkBlue6")
sg.set_options(font='verdana 15')

layout = [
    [sg.Text("Uppercase:"), sg.Push(), sg.Input(size=(15, 1), key='-UPPER-')],
    [sg.Text("Lowercase:"), sg.Push(), sg.Input(size=(15, 1), key='-LOWER-')],
    [sg.Text("Digits:"), sg.Push(), sg.Input(size=(15, 1), key='-DIGITS-')],
    [sg.Text("Symbols:"), sg.Push(), sg.Input(size=(15, 1), key='-SYMBOLS-')],
    [sg.Button("Generate"), sg.Push(), sg.Button("Cancel")],
    [sg.Text("Password"), sg.Push(), sg.Multiline(size=(15, 5), no_scrollbar=True, disabled=True, key='-PASSWORD-')],
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Generate':
        upper_input = values['-UPPER-']
        lower_input = values['-LOWER-']
        digits_input = values['-DIGITS-']
        symbols_input = values['-SYMBOLS-']

        upper = random.sample(string.ascii_uppercase, int(upper_input))
        lower = random.sample(string.ascii_lowercase, int(lower_input))
        digits = random.sample(string.digits, int(digits_input))
        symbols = random.sample(string.punctuation, int(symbols_input))
        total = upper + lower + digits + symbols
        total = random.sample(total, len(total))
        password = ''.join(total)

        window['-PASSWORD-'].update(password)

window.close()
