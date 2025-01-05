from tkinter import *
import tkinter.messagebox as msg
import time

root = Tk()
root.geometry("400x400")
root.wm_maxsize(400, 400)
root.wm_minsize(400, 400)
root.title("Apple-Inspired Calculator by Sima")
root.configure(bg="#1C1C1E")  # Dark background color

# Click function for buttons
def click(event):
    global Scvalue
    text = event.widget.cget("text")  # Get text from button
    if text == "=":
        try:
            value = eval(screen.get())
        except Exception:
            value = "Error"
        Scvalue.set(value)
        screen.update()
    elif text == "C":
        Scvalue.set("")
        screen.update()
    elif text == "X":
        val = Scvalue.get()[:-1]
        Scvalue.set(val)
        screen.update()
    else:
        Scvalue.set(Scvalue.get() + text)
        screen.update()

# Display screen
Scvalue = StringVar()
Scvalue.set("")
screen = Entry(root, textvar=Scvalue, font="Helvetica 20", bg="#2C2C2E", fg="white", bd=0, highlightthickness=1, highlightbackground="#3A3A3C")
screen.pack(fill="x", ipadx=10, ipady=10, pady=10)

# Button creation helper
def create_button(frame, text, bg_color, fg_color, width=4):
    b = Button(frame, text=text, font="Helvetica 15", bg=bg_color, fg=fg_color, bd=0, padx=20, pady=20, width=width)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind("<Button-1>", click)

# Button colors
num_bg = "#3A3A3C"  # Numeric button background
op_bg = "#FF9500"  # Operator button background
func_bg = "#636366"  # Function button background
text_color = "white"  # Text color for all buttons

# Create button frames and buttons
buttons = [
    [("C", func_bg), ("X", func_bg), ("/", op_bg), ("*", op_bg)],
    [("7", num_bg), ("8", num_bg), ("9", num_bg), ("-", op_bg)],
    [("4", num_bg), ("5", num_bg), ("6", num_bg), ("+", op_bg)],
    [("1", num_bg), ("2", num_bg), ("3", num_bg), ("=", op_bg)],
    [("0", num_bg), (".", num_bg)]
]

for row in buttons:
    frame = Frame(root, bg="#1C1C1E")
    frame.pack()
    for (text, bg_color) in row:
        create_button(frame, text, bg_color, text_color)

# Help button
def Help():
    msg.showinfo("Help", "This is a Simple Calculator with Apple-inspired design!")

Button(root, text="Help", command=Help, bg=func_bg, fg=text_color, font="Helvetica 12", bd=0).pack(side=BOTTOM, fill=X, pady=10)

root.mainloop()
