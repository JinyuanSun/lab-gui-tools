import PySimpleGUI as sg
from lab_gui_tools import peptide_mass_calculator

sg.theme('dark grey 9')

# Define the window's contents
layout = [[sg.Text("Enter your peptide sequence:")],
          [sg.Input(key='-PEPTIDE-')],
          [sg.Text("Enter your modification list, eg. H20 and Alkyne is 18.01, 55.04:")],
          [sg.Input(key='-MODIFICATIONS-')],
          [sg.Text(size=(60,2), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Lab_GUI_Tools', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    # window['-OUTPUT-']    .update('Hello ' + values['-INPUT-'].upper() + "! Thanks for trying PySimpleGUI")
    output_path = sg.popup_get_folder('Please enter a folder name')
    peptide = values['-PEPTIDE-']
    modification = [float(x) for x in values['-MODIFICATIONS-'].split(',')]
    # print(modification, type(modification))
    peptide_mass_calculator.peptide_fragment_mass(peptide, modification, output_path)
    window['-OUTPUT-'].update('Fragments of your peptide and mass were saved in ' + output_path + "/frags.csv !")
    # break

# Finish up by removing from the screen
window.close()