from tkinter import *
from functools import partial
import random
import numpy as np
import pandas
import csv

hexdigits = "0123456789ABCDEF"
csvcolor = pandas.read_csv('./colors.csv')
dictColor = {"Red": 1, "Green": 2, "Blue": 3}

class Layout():
    
    def __init__(self):
        self.root = Tk()
        self.color = Label(self.root, text="", bg="black", height=10, width=50)
        self.lastColor = np.array([1, 1, 1])
        self.color["bg"] = self.getNewColor()
        
        bt_red = Button(self.root, text="Red")
        bt_blue = Button(self.root, text="Blue")
        bt_green = Button(self.root, text="Green")

        bt_red["command"] = partial(self.click, bt_red)
        bt_blue["command"] = partial(self.click, bt_blue)
        bt_green["command"] = partial(self.click, bt_green)

        self.color.pack()
        bt_red.pack()
        bt_blue.pack()
        bt_green.pack()
    
    def getNewColor(self):
        newColor = "".join([hexdigits[random.randint(0,0xF)] for _ in range(6) ])
        
        if(self.lastColor != ""):
            # R=0, G=1, B=2
            self.lastColor[0] = int(newColor[:2], 16)
            self.lastColor[1] = int(newColor[2:4], 16)
            self.lastColor[2] = int(newColor[4:], 16)
        newColor = "#"+newColor
        self.color["bg"] = newColor
        
    def click(self, button):
        print(button["text"])
        self.getNewColor()
        addColor(button["text"], self.lastColor)

    def Start(self, size):
        self.root.geometry(size)
        self.root.mainloop()

def addColor(color, rgb):
    data = {'color': dictColor[color], 'r': rgb[0], 'g': rgb[1], 'b':rgb[2]}
    writeCSV(data)
    # newRow = pandas.DataFrame(data=data) 
    # frames = [csv, newRow]
    # newCSV = pandas.concat(frames, ignore_index=True)
    # print(newCSV.head())
    # csv = newCSV

def writeCSV(data):
    with open("./colors.csv", 'a') as csvfile:
        fieldnames = ['color', 'r', 'g', 'b']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

        writer.writerow(data)