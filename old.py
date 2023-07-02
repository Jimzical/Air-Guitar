import PySimpleGUI as sg
import os
from pygame import mixer

def GUI_Builder():
    sg.theme('DarkBrown2')

    layout = []
    layoutcol = []

    # buttons
    for file in os.listdir('samples'):
        # buttons
        layout.append([sg.Button(file[:-4])])
        # checkboxes
        layoutcol.append([sg.Checkbox(file[:-4], default=True, key=file[:-4])])

    col1 = sg.Column(layout, element_justification='c', vertical_scroll_only=True,scrollable=True)
    col2 = sg.Column(layoutcol, element_justification='c', vertical_scroll_only=True,scrollable=True)
    col = [[col1, col2]]
    layout = [[sg.Text('Click the button to play a sound')]]
    layout.append(col)
    layout.append([sg.Button('Play Sound')])
    wind = sg.Window('Sound Player', layout= layout, grab_anywhere=True)
    return wind


def stringDict():
    # d = {0 : 'E4.wav', 1 : 'B3.wav', 2 : 'G3.wav', 3 : 'D3.wav', 4 : 'A2.wav', 5 : 'E2.wav'}
    d = {'e' : 'E4.wav', 'B' : 'B3.wav', 'G' : 'G3.wav', 'D' : 'D3.wav', 'A' : 'A2.wav', 'E' : 'E2.wav'}
    return d

def Em():
    d = stringDict()
    d['A'] = "B2.wav"
    d['D'] = "E3.wav"
    index = 0
    for key in d:
        mixer.Channel(index).play(mixer.Sound('samples/' + d[key]))
        index += 1


def D():
    d = stringDict()
    # removeing stringe
    d.pop('E')
    d.pop('A')
    d['G'] = 'A3.wav'
    d['B'] = 'D4.wav'
    d['e'] = 'Fs4.wav'
    index = 0
    for key in d:
        mixer.Channel(index).play(mixer.Sound('samples/' + d[key]))
        index += 1
# make a funtion for D chord

def main():
    window = GUI_Builder()
    samplelist = []
    for file in os.listdir('samples'):
        samplelist.append(file[:-4])
    print(samplelist)

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED:
            break
        if event in samplelist:
            print('Playing sound', event)
            # give varible e2 the sound
            sound = mixer.Sound('samples/' + event + '.wav')
            sound = mixer.Channel(0).play(sound)
            # sound.play()
        if event == 'Play Sound':
            print('Playing sound')
            # Em()
            D()

            # for file in samplelist:
            #     if values == True:
            #         sound = mixer.Sound('samples/' + file + '.wav')
            #         sound.play()

       
if __name__ == '__main__':
    mixer.init()
    main()


