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

#Back Buttom
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

#Current Username
current_username=Label(win,
                text='Current Username:',
                   font=('Arial',15, 'bold'),
                   fg='Black',
                   bg='white')
current_username.place(x=45, y=100)

current_username_entry = Entry(win,
                           font=('Arial', 15),
                                 width=17,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
current_username_entry.place(x=230, y=100)

#New Username
new_username=Label(win,
                text='New Username:',
                   font=('Arial',15, 'bold'),
                   fg='Black',
                   bg='white')
new_username.place(x=70, y=180)

new_username_entry = Entry(win,
                           font=('Arial', 15),
                                 width=17,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
new_username_entry.place(x=230, y=180)

#Change Buttom
def change_click():
    # Connect to the database
    database = sqlite3.connect('project.db')
    cursor = database.cursor()

    current_username= current_username_entry.get()
    new_username= new_username_entry.get()

    cursor.execute("UPDATE customer_information SET username=? WHERE username=?",(new_username, current_username))
    
    current_username_entry.delete(0,END)
    new_username_entry.delete(0,END)

    # Commit and close connection to Database
    database.commit()
    database.close()

    win.destroy()
    subprocess.run(['python','login_register.py'])




change_buttom = Button(win,
                     text='Change',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=change_click)
change_buttom.place(x=235, y=250)


# Commit and close connection to Database
database.commit()
database.close()



mainloop()