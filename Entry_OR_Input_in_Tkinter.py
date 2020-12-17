from tkinter import *
root = Tk()
root.geometry('600x600')

def hello_user():
    name_display = Label(root, text="Hello, "+name.get())
    name_display.pack()

name = Entry(root)
name.pack()

hello_button = Button(root, text="Say Hello", command=hello_user)
hello_button.pack()

root.mainloop()