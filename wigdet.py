from tkinter import *
from datetime import date
window = Tk()
window.title("Super Duper Secure Thing.exe.")
window.geometry("500x700")
label = Label(text ="Super Duper Secure Password Thing:")
namelabel = Label(text ="Enter your name:")
nentry = Entry()
def Display():
    name = nentry.get()
    global message 
    message = "\nYou have been doomed. You will die on 11:59pm\n on "
    day = f"Hello {name}"
    tbox.insert(END,day)
    tbox.insert(END,message)
    tbox.insert(END,date.today())
tbox = Text(height=24)
button = Button(text="DO NOT PRESS!",bg="black",fg="white",command=Display)
label.pack()
namelabel.pack()
nentry.pack()
button.pack()
tbox.pack()
window.mainloop()