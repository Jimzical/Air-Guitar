# write a code to select all the files that end with .wav in sample folder and display them in a listbox

import os
import PySimpleGUI as sg


def FileNameGetter(path,filetype = '.wav'):
    files = os.listdir(path)
    file_list = []
    for file in files:
        if file.endswith(filetype):
            print(file)
            file_list.append(file)

    return file_list

def FileSaving(OriginalDestination, NewDestination, filelist):
    for file in filelist:
        # print("File: {}, Original Destination: {}, New Destination: {}".format(file, OriginalDestination, NewDestination))
        os.rename(OriginalDestination + file, NewDestination + file)
        print(file + ' has been moved to ' + NewDestination)


def TempFix(filelist):
    # rename all files in samples from guitarXX.wav to XX.wav
    for file in filelist:
        # print(file)
        os.rename('samples/' + file, 'samples/' + file[6:])
        print(file + ' has been renamed to ' + file[6:])
def main():
    acoustics = FileNameGetter('samples/guitar-acoustic/')
    # electric = FileNameGetter('samples/guitar-electric/')
    print(acoustics)
    print('-'*100)
    FileSaving('samples/guitar-acoustic/', 'samples/guitar', acoustics)
if __name__ == '__main__':
    # main()    
    TempFix(FileNameGetter('samples/'))