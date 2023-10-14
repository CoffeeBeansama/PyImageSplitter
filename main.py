#!/usr/bin/env python3


import cv2
import tkinter as tk
from tkinter import filedialog
from tkfilebrowser import askopenfilename



font = ("Roboto-Medium.ttf",40)
font2 = ("Roboto-Medium.ttf",28)


window = tk.Tk()
window.title("Image Splitter")

window.geometry("400x200")

#region browseFile
def browseFile():
    file = askopenfilename(parent=window, initialdir=' ', initialfile='png',
                           filetypes=[("Pictures", "*.png|*.jpg|*.JPG"),
                                      ("All files", "*")])
    return str(file)

#endregion

rowText = tk.Label(window,text="Rows",font=font2)
columnText = tk.Label(window,text="Column",font=font2)
row = tk.Entry(window)
column = tk.Entry(window)

rowText.place(x=40,y=20)
columnText.place(x=235,y=20)
row.place(x=10,y=60)
column.place(x=225,y=60)

#region main function
def sliceImage():
    try:
        path = browseFile()
        img = cv2.imread(path)
        img2 = img
        height, width, channels = img.shape
        # Number of pieces Horizontally
        W_SIZE = int(column.get())
        textToRemove = []

        # Number of pieces Vertically to each Horizontal
        H_SIZE = int(row.get())
        imgFile = ""
        for ih in range(H_SIZE):
            for iw in range(W_SIZE):
                x = width / W_SIZE * iw
                y = height / H_SIZE * ih
                h = (height / H_SIZE)
                w = (width / W_SIZE)
                img = img[int(y):int(y + h), int(x):int(x + w)]

                for i in path[::-1]:
                    if i != "/":
                        textToRemove.append(i)
                    else:
                        for j in textToRemove[::-1]:
                            imgFile += j
                        break
                savePath = path.replace(imgFile,"")

                cv2.imwrite(savePath + str(ih) + str(iw) + ".png", img)
                img = img2
    except: pass

#endregion

sliceButton = tk.Button(window,text="Browse Image",command=sliceImage)
sliceButton.place(x=145,y=120)

window.mainloop()