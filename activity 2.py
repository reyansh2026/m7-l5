from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
root=Tk()
root.title("Denominations Calculator")
root.geometry("500x500")
large=Font(family="Times New Roman",size=20)
medium=Font(family="Arial", size=12)
a=Label(root,text="Welcome to the \nDenominations Calculator!", font=large,fg="black", bg="#e0e0e0")
a.place(x=100,y=200)
def clicked():
    messagebox.showinfo("Denominations Calculator", "You are about to calculate denominations.")
    top=Toplevel()
    top.title("Calculator")
    top.geometry("400x400")
    k=Label(top,text="",relief=RIDGE, fg="black", bg="gray",width=53,height=25)
    k.place(x=10,y=10)
    c=Label(top,text="Enter the amount:", font=medium, fg="black", bg="lightgray")
    c.place(x=140,y=40)
    d=Entry(top, fg="black", bg="white", width=30)
    d.place(x=110,y=80)
    g=Label(top,text=f"The number of 2000 rupee notes is:", relief=GROOVE, fg="black", bg="lightgray")
    h=Label(top,text=f"The number of 500 rupee notes is:", relief=GROOVE, fg="black", bg="lightgray")
    i=Label(top,text=f"The number of 100 rupee notes is:", relief=GROOVE, fg="black", bg="lightgray")
    j=Label(top,text=f"The number of 1 rupee notes is:", relief=GROOVE, fg="black", bg="lightgray")
    g.place(x=40,y=200)
    h.place(x=40,y=250)
    i.place(x=40,y=300)
    j.place(x=40,y=350)
    def entered():
        f=int(d.get())
        notes=f//2000
        notes1=(f%2000)//500
        notes2=(f%500)//100
        notes3=(f%100)//1
        l=Label(top,text=f" {notes} ", relief=SUNKEN, fg="black", bg="#e0e0e0")
        l.place(x=260,y=200)
        m=Label(top,text=f" {notes1} ", relief=SUNKEN, fg="black", bg="#e0e0e0" )
        m.place(x=260,y=250)
        n=Label(top,text=f" {notes2} ", relief=SUNKEN, fg="black", bg="#e0e0e0")
        n.place(x=260,y=300)
        o=Label(top,text=f" {notes3} ", relief=SUNKEN, fg="black", bg="#e0e0e0")
        o.place(x=260,y=350)
    e=Button(top,text="Calculate",relief=GROOVE, fg="white", bg="darkred",command=entered,width=10)
    e.place(x=160,y=120)
    top.mainloop()
b=Button(root,text="Let's get started!",relief=RAISED, fg="white", bg="darkred", command=clicked,height=1,width=15)
b.place(x=180,y=300)
root.mainloop()