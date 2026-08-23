import tkinter as tk

window = tk.Tk()
window.title("THE LOGIN APP")
window.geometry("1200x900")
window.configure(bg="#CCFF00")  # Blinding chartreuse background

# Main frame with chaotic background
frame = tk.Frame(window, height=800, width=1000, bg="#FF007F")
frame.place(x=10, y=10)

# Unreadable header
title_label = tk.Label(
    frame,
    text="W E L C O M E   T O   L O G I N",
    font=("Comic Sans MS", 32, "bold"),
    fg="#00FF00",  # Neon green on hot pink
    bg="#FF007F",
)
title_label.place(x=50, y=10)

# 1. Full Name
l1 = tk.Label(
    frame,
    text="Full Name:",
    font=("Impact", 12),
    fg="#000000",
    bg="#FF007F",
)
l1.place(x=10, y=80)
n1 = tk.Entry(frame, font=("Courier", 10), bg="#000000", fg="#00FF00")
n1.place(x=300, y=80)

# 2. Email Address
l2 = tk.Label(frame, text="Email Address:", font=("Papyrus", 12, "bold"), bg="#FF007F")
l2.place(x=10, y=120)
n2 = tk.Entry(frame, width=3)
n2.place(x=300, y=120)

# 3. Enter Password
l3 = tk.Label(
    frame, text="Enter Password:", font=("Arial", 12, "bold"), bg="#FF007F", fg="#FFFF00"
)
l3.place(x=10, y=160)
n3 = tk.Entry(frame, show="🤡")
n3.place(x=300, y=160)

# 4. Enter Password Again
l4 = tk.Label(
    frame, text="Enter Password Again:", font=("Arial", 12, "bold"), bg="#FF007F", fg="#FFFF00"
)
l4.place(x=10, y=190)
n4 = tk.Entry(frame, show="🤡")
n4.place(x=300, y=190)

# 5. Enter Phone Number - Clear label, slider control
l5 = tk.Label(
    frame,
    text="Enter Phone Number (Slide to select your exact 10-digit number):",
    font=("Arial", 11, "bold"),
    bg="#FF007F",
    fg="white",
)
l5.place(x=10, y=220)
phone_slider = tk.Scale(
    frame, from_=1000000000, to=9999999999, orient=tk.HORIZONTAL, length=500
)
phone_slider.place(x=10, y=245)

# 6. Enter OTP
l6 = tk.Label(
    frame,
    text="Enter OTP:",
    font=("Arial", 11, "bold"),
    bg="#FF007F",
)
l6.place(x=10, y=300)
n6 = tk.Entry(frame, width=10)
n6.place(x=300, y=300)


# Function to display original message
def Display():
    name = n1.get()
    message = f"Hey {name}\nCongrats on your new account, did you verify it yet?"
    tbox.delete("1.0", tk.END)
    tbox.insert(tk.END, message)


# Stationary submit button
button = tk.Button(
    frame,
    text="Create Account",
    bg="#00FF00",
    fg="#000000",
    font=("Arial", 12, "bold"),
    command=Display,
)
button.place(x=50, y=360)

# Output text box
tbox = tk.Text(frame, height=6, width=50, bg="#FFFF00", fg="#FF0000", font=("Comic Sans MS", 10))
tbox.place(x=50, y=430)

window.mainloop()