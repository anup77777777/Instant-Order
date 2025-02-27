from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3

# Connect to the database
database = sqlite3.connect('project.db')
cursor = database.cursor()

#Windows
win = Tk()
win.title('Instant Order')
win.geometry('600x500')
win.configure(bg='white')
logo = PhotoImage(file='instantorder_logowithoutbg.png')
win.iconphoto(True, logo)

#Back Button
def back_click():
    win.destroy()
    
back_button = CTkButton(win,
                text="Back",
                font=("Arial", 15,'bold'),
                corner_radius=500,
                height=30,
                width=30,
                text_color='black',
                fg_color='#d40707',
                bg_color='white',
                hover_color='#fc0303',
                command=back_click)
back_button.place(x=5, y=10)

#Username
username=Label(win,
                text='Username:',
                   font=('Arial',15, 'bold'),
                   fg='Black',
                   bg='white')
username.place(x=110, y=100)

username_entry = Entry(win,
                           font=('Arial', 15),
                                 width=17,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
username_entry.place(x=230, y=100)

#Password
password=Label(win,
                text='Password:',
                   font=('Arial',15, 'bold'),
                   fg='Black',
                   bg='white')
password.place(x=110, y=180)

password_entry = Entry(win,
                           font=('Arial', 15),
                                 width=17,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
password_entry.place(x=230, y=180)

#Delete BUtton
def delete_click():
    # Connect to the database
    database = sqlite3.connect('project.db')
    cursor = database.cursor()

    username= username_entry.get()
    password= password_entry.get()

    cursor.execute("DELETE from customer_information WHERE username=? AND password=?",(username, password))
    
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    # Commit and close connection to Database
    database.commit()
    database.close()

    win.destroy()
    subprocess.run(['python','login_register.py'])




delete_buttom = Button(win,
                     text='Delete Account',
                     font=('Arial', 15, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=delete_click)
delete_buttom.place(x=215, y=250)


# Commit and close connection to Database
database.commit()
database.close()



mainloop()