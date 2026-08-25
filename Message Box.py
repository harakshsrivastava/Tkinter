from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("2560x1600")
def Message():
    messagebox.showwarning("YOU HAVE A VIRUS!!!!!!!!!!!!DEFINITLY NOT FAKE!!!!!!!!!","YOU HAVE TO OPEN THE HARD DRIVE AND GIVE IT A BATH")
button = Button(text="OK",command=Message)
button.pack()
window.mainloop()
