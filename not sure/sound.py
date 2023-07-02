# # # from pydub import AudioSegment
# # # from pydub.playback import play

# # # # Load the sound file
# # # sound = AudioSegment.from_file(r"C:\Users\arish\Downloads\cc.wav", format="wav")

# # # # Play the sound
# # # play(sound)


# # # import sounddevice as sd
# # # import numpy as np

# # # # load the sound
# # # data, samplerate = sd.read("cc.wav")

# # # # play the sound
# # # sd.play(data, samplerate)


# # import sounddevice as sd
# # import soundfile as sf

# # # print(sd.query_devices())
# # # print(sd.default.device)
# # # print(sd.default.samplerate)
# # print('loading sound')
# # # load the sound
# # data, samplerate = sf.read("cc.wav")
# # sd.play(data, samplerate)
# # status = sd.wait()

# # sd.play(data, samplerate)
# # status = sd.wait()

# # # n=0

# # # while True:
# # #     # if q is pressed, exit the loop
# # #     if n<3:
# # #         print('playing sound')

# # #         # play the sound
# # #         sd.play(data, samplerate)

# # #         # wait for the sound to finish playing
# # #         status = sd.wait()

# # #         print('done')
# # #     n+=1        



# import PySimpleGUI as sg
# import soundfile as sf
# import sounddevice as sd
# import numpy as np

# # create a global variable to store the current output stream
# output_stream = None

# def play_sound(file_path):
#     global output_stream
#     data, samplerate = sf.read(file_path)

#     # if there is an existing output stream, stop it
#     if output_stream is not None:
#         output_stream.stop()

#     # create a new output stream
#     play_callback(data,samplerate)
#     output_stream = sd.OutputStream(callback=play_callback, samplerate=samplerate)
#     output_stream.start()

# def play_callback(outdata, frames):
#     outdata[:] = data
#     data = data[frames:]    

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


#         # data, samplerate = sf.read("cc.wav")
#         # sd.play(data, samplerate)
#         # status = sd.wait()


import PySimpleGUI as sg
import soundfile as sf
import sounddevice as sd

# create a global variable to store the current output stream
output_stream = None

def play_sound(file_path):
    global output_stream
    data, samplerate = sf.read(file_path)

    # if there is an existing output stream, stop it
    if output_stream is not None:
        output_stream.stop()

    # create a new output stream
    output_stream = sd.OutputStream(callback=lambda x,y: play_callback(x,y,data), samplerate=samplerate)

    output_stream.start()

def play_callback(outdata, frames, data):
    outdata[:] = data[:frames]
    data = data[frames:]

def GUI():
    sg.theme('DarkBrown2')

    layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound')]]
    wind = sg.Window('Sound Player', layout)
    return wind

if __name__ == '__main__':
    global data

    wind = GUI()

    while True:
        event, values = wind.read()
        if event == sg.WIN_CLOSED:
            print('Window closed')
            break
        if event == 'Play Sound':
            print('Playing sound')
            # play the sound
            play_sound("cc.wav")
