import PySimpleGUI as sg
# import pygame as pg
from pygame import mixer

def GUI_Builder():
    sg.theme('DarkBrown2')

    # layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound 1'), sg.Button('Play Sound 2'), sg.Button('Play 2 Sounds Together')  ]]
    layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound A2')], [sg.Button('Play Sound B3')] , [sg.Button('Play Sound D3')], [sg.Button('Play Sound E2')], [sg.Button('Play Sound E4')], [sg.Button('Play Sound G3') ],\
               [sg.Checkbox('Play Sound A2', default=True, key='A2')], [sg.Checkbox('Play Sound B3', 'B3', key='B3')], [sg.Checkbox('Play Sound D3', 'D3', key='D3')], [sg.Checkbox('Play Sound E2', 'E2', key='E2')], [sg.Checkbox('Play Sound E4', 'E4', key='E4')], [sg.Checkbox('Play Sound G3', 'G3', key='G3')], [sg.Button('Play Sound')]]
    # q: how to get radio buttons to work in pysimplegui
    # a: https://stackoverflow.com/questions/62036500/how-to-use-radio-buttons-in-pysimplegui
    wind = sg.Window('Sound Player', layout)
    return wind

def main():
    window = GUI_Builder()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Play Sound A2':
            print('Playing sound A2')
            # give varible e2 the sound
            a2 = mixer.Sound('Media/A2.wav')
            a2.play()
        if event == 'Play Sound B3':
            print('Playing sound B3')
            # give varible e2 the sound
            b3 = mixer.Sound('Media/B3.wav')
            b3.play()
        if event == 'Play Sound D3':
            print('Playing sound D3')
            # give varible e2 the sound
            d3 = mixer.Sound('Media/D3.wav')
            d3.play()
        if event == 'Play Sound E2':
            print('Playing sound E2')
            # give varible e2 the sound
            e2 = mixer.Sound('Media/E2.wav')
            e2.play()
        if event == 'Play Sound E4':
            print('Playing sound E4')
            # give varible e2 the sound
            e4 = mixer.Sound('Media/E4.wav')
            e4.play()
        if event == 'Play Sound G3':
            print('Playing sound G3')
            # give varible e2 the sound
            g3 = mixer.Sound('Media/G3.wav')
            g3.play()
        
        if event == 'Play Sound':
            print('Playing sound')
            if values['A2'] == True:
                a2 = mixer.Sound('Media/A2.wav')
                a2.play()
            if values['B3'] == True:
                b3 = mixer.Sound('Media/B3.wav')
                b3.play()
            if values['D3'] == True:
                d3 = mixer.Sound('Media/D3.wav')
                d3.play()
            if values['E2'] == True:
                e2 = mixer.Sound('Media/E2.wav')
                e2.play()
            if values['E4'] == True:
                e4 = mixer.Sound('Media/E4.wav')
                e4.play()
            if values['G3'] == True:
                g3 = mixer.Sound('Media/G3.wav')
                g3.play()




                
        # if event == 'Play Sound 1':
        #     print('Playing sound 1')
        #     # give varible e2 the sound
        #     e2 = mixer.Sound('Media/E2.wav')
        #     e2.play()
        # if event == 'Play Sound 2':
        #     print('Playing sound 2')
        #     # give varible e2 the sound
        #     e4 = mixer.Sound('Media/E4.wav')
        #     e4.play()
        # if event == 'Play 2 Sounds Together':
        #     print('Playing 2 sounds')
        #     # give varible e2 the sound
        #     e2 = mixer.Sound('Media/E2.wav')
        #     e2.play()
        #     e4 = mixer.Sound('Media/E4.wav')
        #     e4.play()

if __name__ == '__main__':
    # pg.mixer.init()
    mixer.init()
    main()



