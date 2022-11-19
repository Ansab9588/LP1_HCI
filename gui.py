# importing everything from tkinter module 
from cProfile import label
from tkinter import *
from tkinter import messagebox

# creating window/screen/login page
# using tk class from tkinter module, creating a window
# also creating a instance (ie tk)  / it can be anything, not keyword specific
tk=Tk()

# title of the page using 'title()' function
tk.title("Login System")

# changing size of the page using 'geometry()' function
tk.geometry("350x300")

# to hide the maximize option from the window, we use 'resizable()' function
tk.resizable(False,False)

# changing background colour of the window using 'configure()' function
tk.configure(bg="pink")

# creating alerts and message boxes for showing failures and success
def login():
    username=entry1.get()
    password=entry2.get()
    if(username=="shelby" and password=="thomas"):
        messagebox.showinfo("Welcome", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")    


# assign heading using 'label()' and 'pack()' functions
# we can also use fore ground (ie fg in the 'text' to change the text color)
Label(tk,text="LOGIN PAGE", font="calibri 30 bold", bg="pink").pack() 

# creating username label
Label(tk,text="USERNAME : ", font="aerial 10 bold", bg="pink").place(x=40,y=90)

# creating password label
Label(tk,text="PASSWORD : ", font="aerial 10 bold", bg="pink").place(x=40,y=130)

# creating an entry widget / Text Box for 'username'
# bd is used for the border of the text box
entry1=Entry(tk, bd=4)
entry1.place(x=140,y=90)

# creating an entry widget / Text Box for 'password'
entry2=Entry(tk, bd=4, show="*")
entry2.place(x=140,y=130)

# creating a button for 'Login'
Button(tk, text="Login", bg="black", fg="pink", bd=4, command=login).place(x=100,y=190)

# creating a button for 'Cancel'
Button(tk, text="Cancel", bg="black", fg="pink", bd=4).place(x=190,y=190)


# creating a mainloop() function, because of it, the window will show
mainloop()
