import mantisclaw
from tkinter import Tk, Label, Button

def click_action(button):
    button.config(text=f"Results:")

root = Tk()
root.title('Mantisclaw')
root.geometry("1000x800")


label = Label(root, text="Welcome to Mantisclaw", font=42, fg="Black")
label.pack()

click_button = Button(root, text="Search", width=12)
click_button.pack()

root.mainloop()