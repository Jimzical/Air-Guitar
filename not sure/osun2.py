# import PySimpleGUI as sg
# import soundfile as sf
# import sounddevice as sd
# import numpy as np

# # create a global variable to store the current output
# output = None

# def play_sound(file_path):
#     global output
#     data, samplerate = sf.read(file_path)
#     # if there is an existing output, stop it
#     if output is not None:
#         output.stop()
#     # create a new output
#     output = sd.Output(samplerate=samplerate, channels=2)
#     output.start(data)



# sg.theme('DarkBrown2')
# layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound')]]
# wind = sg.Window('Sound Player', layout)

# while True:
#     event, values = wind.read()
#     if event == sg.WIN_CLOSED:
#         print('Window closed')
#         break
#     if event == 'Play Sound':
#         print('Playing sound')
#         # play the sound
#         play_sound("cc.wav")


import PySimpleGUI as sg
import soundfile as sf
import sounddevice as sd

# create a global variable to store the current sound file data and sample rate
current_data = None
current_samplerate = None

def play_sound(file_path):
    global current_data
    global current_samplerate
    # stop any current sound that is playing
    sd.stop()
    # read the sound file and store the data and sample rate in global variables
    current_data, current_samplerate = sf.read(file_path)
    # play the sound
    sd.play(current_data, current_samplerate)

sg.theme('DarkBrown2')

layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound')]]
wind = sg.Window('Sound Player', layout)

while True:
    event, values = wind.read()
    if event == sg.WIN_CLOSED:
        print('Window closed')
        break
    if event == 'Play Sound':
        print('Playing sound')
        # play the sound
        play_sound("cchord.wav")
