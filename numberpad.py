from tkinter import *
window = Tk()
window.title("Number Pad")
window.geometry("300x400")
var = [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=100)
    window.rowconfigure(i,weight=1,minsize=100)
    for j in range(3):
        frame = Frame(window,relief=RIDGE,borderwidth=2)
        frame.grid(row= i, column= j)
        label = Label(frame,text=var[i][j])
        label.pack(padx=4,pady=4)
window.mainloop()