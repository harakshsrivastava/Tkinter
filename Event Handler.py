from math import *
from tkinter import *
print(pi)
window = Tk()
window.geometry("600x600")
window.title("VIRUS.EXE")
def Keypresses(event):
    print(event.char)
window.bind("<Key>",Keypresses)
def Click(event):
    print("Mouse Disabled.")
button = Button(text=pi)
button.pack()
button.bind("<Button-1>",Click)
window.mainloop()
