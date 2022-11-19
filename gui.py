from cProfile import label
from tkinter import *
from tkinter import messagebox


tk=Tk()

tk.title("Login System")

tk.geometry("350x300")

tk.resizable(False,False)

tk.configure(bg="pink")

def login():
    username=entry1.get()
    password=entry2.get()
    if(username=="shelby" and password=="thomas"):
        messagebox.showinfo("Welcome", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")    


Label(tk,text="LOGIN PAGE", font="calibri 30 bold", bg="pink").pack() 

Label(tk,text="USERNAME : ", font="aerial 10 bold", bg="pink").place(x=40,y=90)

Label(tk,text="PASSWORD : ", font="aerial 10 bold", bg="pink").place(x=40,y=130)

entry1=Entry(tk, bd=4)
entry1.place(x=140,y=90)

entry2=Entry(tk, bd=4, show="*")
entry2.place(x=140,y=130)

Button(tk, text="Login", bg="black", fg="pink", bd=4, command=login).place(x=100,y=190)

Button(tk, text="Cancel", bg="black", fg="pink", bd=4).place(x=190,y=190)


mainloop()
