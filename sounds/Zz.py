import PySimpleGUI as sg
import pygame as pg


def GUI_Builder():
    sg.theme('DarkBrown2')

    layout = [[sg.Text('Click the button to play a sound')],[sg.Button('Play Sound')]]
    wind = sg.Window('Sound Player', layout)
    return wind

def main():
    window = GUI_Builder()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Play Sound':
            print('Playing sound')
            # give varible e2 the sound
            e2 = pg.mixer.Sound('E2.wav')
            # play the sound
            e2.play()
            # print(pg.mixer.music.load('E2.wav'))
            # pg.mixer.music.play()
            # while pg.mixer.music.get_busy():
            #     pg.time.Clock().tick(10)
            # sg.Popup('You clicked the button')


if __name__ == '__main__':
    pg.mixer.init()
    main()



