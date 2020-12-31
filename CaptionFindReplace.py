import os
import csv
import json
from tkinter import *
from tkinter import filedialog

def browseFiles():
    directoryList = os.getcwd() 

    # Root context object
    # root = Tk()

    # The filetypes *IN TCL FORMAT*
    filetypes = "{{csv files} *.csv} {{all files} *}"

    # The actual call; note that that that's a very unusual command name by Tcl standards!
    # 
    fileString = window.tk.eval('::tk::dialog::file:: open -filetypes {' + filetypes + '}')

    
    fileNameEnd = len(fileString)
    fileNameStart = fileString.rfind('/')
    fileName = fileString[fileNameStart+1:fileNameEnd]

    # Fix up the result; empty string means "no file selected"
    if fileString == "":
        fileString = None

    with open(fileName, 'r', encoding='utf-8-sig') as csvFile:
        readCSV = csv.reader(csvFile)
        for line in readCSV:
            wordDict = dict((k[0], k[1]) for k in readCSV)
        with open('wordList.json', 'w') as wordDictionary:
            json.dump(wordDict, wordDictionary)
    
    # Change label contents 
    labelSelectedFile.configure(text="File Opened: "+fileName, fg = 'blue')

def processFile():
    directoryList = os.getcwd() 

    # Root context object
    # root = Tk()

    # The filetypes *IN TCL FORMAT*
    filetypes = "{{all files} *}"

    # The actual call; note that that that's a very unusual command name by Tcl standards!
    # 
    fileString = window.tk.eval('::tk::dialog::file:: open -filetypes {' + filetypes + '}')

    
    fileNameEnd = len(fileString)
    fileNameStart = fileString.rfind('/')
    fileName = fileString[fileNameStart+1:fileNameEnd]

    # Fix up the result; empty string means "no file selected"
    if fileString == "":
        fileString = None

    with open(fileName, 'r', encoding='utf-8-sig') as captionFile:
        readFile = captionFile.readlines()
        saveFile = open('correctedcaption.txt', 'a', encoding='utf-8-sig')
        with open('wordList.json') as jsonFile:
            wordList = json.load(jsonFile)
            for line in readFile:
                for key, value in wordList.items():
                    line = line.replace(key, value)
                saveFile.write(line)
                 
    # Change label contents 
    labelProcessedFile.configure(text="File Processed: "+fileName, fg = 'blue')

    processComplete()
    

def processComplete(): 
    window2 = Tk()
    window2.title('Process Complete')
    window2.geometry('260x50')
    window2.config(background='white')
    labelStatus = Label(window2,
                        text = 'Process Complete', font=('Arial', 20),
                        width = 0, height = 1,
                        fg = 'blue', background='white')  
    labelStatus.place(x = 18, y = 0)
    window2.after(5000, lambda: window2.destroy())
    window.after(8000, lambda: window.destroy())

window = Tk()
window.title('Caption Find and Replace')
window.geometry('500x260')
window.config(background='white')

# Code to add widgets will go here...
labelApplication = Label(window,
                            text = 'Caption Find and Replace Application',
                            width = 0, height = 1, font=('Arial', 20),
                            fg = 'blue', background='white')

labelSelectFile = Label(window,
                            text = 'Click the button below to select the .csv file containing your \ncommonly misspelled words and corrections.',
                            width = 45, height = 2, justify = LEFT, background='white')

buttonSelectFile = Button(window,
                            text = 'Select Words File',
                            command = browseFiles)
labelSelectedFile = Label(window,
                            text = 'File Selected: ', background='white')

labelProcessFile = Label(window,
                            text = 'Click the button below to select and process the caption file.',
                            background='white')

buttonProcessCaptionFile = Button(window,
                                    text = 'Select Caption File',
                                    command = processFile)

labelProcessedFile = Label(window,
                            text = 'File Processed: ', background='white')

labelApplication.place(x = 18, y = 5)

labelSelectFile.place(x = 18, y = 60)

buttonSelectFile.place(x = 18, y = 110)

labelSelectedFile.place(x = 150, y = 119)

labelProcessFile.place(x = 18, y = 150)

buttonProcessCaptionFile.place(x = 18, y = 185)

labelProcessedFile.place(x = 150, y = 194)

window.mainloop()