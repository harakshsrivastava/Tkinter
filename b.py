import tkinter as tk
from tkinter import messagebox
def on_key_press(event):
    print(f"Last character typed: {event.char}")
def on_area_click(event):
    print("Routine area clicked!")
def show_next_task():
    task = entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "No task entered!")
    else:
        label_result.config(text=f"Next Task: {task}")
root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("400x300")
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Key>", on_key_press)
area_label = tk.Label(root, text="Click inside this area", bg="lightgray", width=30, height=5)
area_label.pack(pady=10)
area_label.bind("<Button-1>", on_area_click)
btn_next = tk.Button(root, text="Show Next Task", command=show_next_task)
btn_next.pack(pady=5)
label_result = tk.Label(root, text="")
label_result.pack(pady=10)
root.mainloop()