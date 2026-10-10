from tkinter import *
root=Tk()
root.title("Main window")
root.geometry('500x500')
def clicked():
    top=Toplevel()
    top.title("Top window")
    top.geometry("200x200")
    top.mainloop()
a=Button(root,text="Click me", fg="black", bg="white", command=clicked)
a.pack()
root.mainloop()
