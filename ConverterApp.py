import PySimpleGUI as sg

layout = [
    [
     sg.Input(key = '-INPUT-'),
     sg.Spin(['km to mi', 'kg to lb', 'sec to min'], key = '-SPIN-'),
     sg.Button('Convert', key = '-BUTTON-'),
     sg.Button('Exit', key = '-CLOSE-')
     ],
    [sg.Text(key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
 
    if event == sg.WIN_CLOSED:
        break
    if event == '-CLOSE-':
        window.close()
    
    if event == '-BUTTON-':
        input_val = values['-INPUT-']
        if input_val.isnumeric() and (float(input_val) >= 0.0):
            if(values['-SPIN-'] == 'km to mi'):
                output = round(float(input_val) / 1.609344, 2)
                answer = f'{input_val} Kilometers are {output} Miles.'
                window['-OUTPUT-'].update(answer)
            if(values['-SPIN-'] == 'kg to lb'):
                output = round(float(input_val) * 2.205, 2)
                answer = f'{input_val} Kilograms are {output} Pounds.'
                window['-OUTPUT-'].update(answer)
            if(values['-SPIN-'] == 'sec to min'):
                output = round(float(input_val) / 60, 2)
                answer = f'{input_val} Seconds are {output} Minutes.'
                window['-OUTPUT-'].update(answer)  
        else:
            window['-OUTPUT-'].update('Error: Input is not a number greater than zero!')


window.close()
