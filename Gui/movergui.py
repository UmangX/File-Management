from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox

def rungui():
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    filed(folder_selected)

    

def filed(data):
    file = open('dta.txt','a+')
    file.write(data)
    file.close()


    

def gui():
    window = Tk() 

    window.geometry('350x200')

    window.title('Umangx mover')

    label = Label(window, text = 'Select The Destiny Directory')

    label.grid(column=1 ,row=5)

    btn = Button(window, text="Select",command=rungui) 

    btn.grid(column=20, row=5)

    window.mainloop()


file = open("dta.txt",'a+')
data = file.readlines()

if data != []:
    print('Nothing')
else:
    gui()   
