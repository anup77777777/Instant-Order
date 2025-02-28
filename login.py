from customtkinter import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import sqlite3

# Connect to the database
database = sqlite3.connect('project.db')
cursor = database.cursor()

#Window
win= CTk()
win.geometry('1920x1080')
set_appearance_mode('light')
win.iconbitmap('instantorder_logowithoutbg.ico')
win.title('Instant Order')

#Logo Image
logo_image= PhotoImage(file='instantorder_logo.png')
original_logo_image = Image.open("instantorder_logo.png")
resized_logo_image = original_logo_image.resize((800, 600), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo_image)
logo_label = CTkLabel(win, text='', image=logo_image, bg_color="transparent")
logo_label.place(x=30, y=40)

#Discription
discription1= CTkLabel(win, text='"Instant Order" is a simple and efficient application that',
                   font= ('Arial', 20, 'italic'),
                   bg_color="transparent",
                   text_color='black')
discription1.place(x=100, y=400)

discription2= CTkLabel(win, text='allows you to place orders directly from a predefined menu.',
                   font= ('Arial', 20, 'italic'),
                   bg_color="transparent",
                   text_color='black')
discription2.place(x=100, y=440)

discription3= CTkLabel(win, text='With just a few taps, you can select your items, confirm',
                    font= ('Arial', 20, 'italic'),
                   bg_color="transparent",
                   text_color='black')
discription3.place(x=100, y=480)

discription4= CTkLabel(win, text='your order, and receive an instant bill.',
                    font= ('Arial', 20, 'italic'),
                   bg_color="transparent",
                   text_color='black')
discription4.place(x=100, y=520)

discription5= CTkLabel(win, text='No hassle, no waiting—just quick and seamless ordering!',
                    font= ('Arial', 20, 'italic'),
                   bg_color="transparent",
                   text_color='black')
discription5.place(x=100, y=560)

#frame
frame= CTkFrame(win, fg_color='lightgray', width=600, height=400, corner_radius=15)
frame.place(x=900, y=250)

#Username
username=CTkLabel(win,
                text="Username:",
                bg_color='lightgray',
                font=("Arial", 30,),
                text_color= 'black')
username.place(x=940, y=350)
username_entry = CTkEntry(win,
                           font=("Arial", 25,),
                           bg_color='lightgray',
                           height=40,
                           width=250,
                           corner_radius=0,
                           border_width=3,
                           border_color='#d40707')
username_entry.place(x=1100, y=350)

#Password
password=CTkLabel(win,
                text="Password:",
                font=("Arial", 30,),
                bg_color='lightgray',
                text_color= 'black')
password.place(x=940, y=430)
password_entry = CTkEntry(win,
                           font=("Arial", 25,),
                           bg_color='lightgray',
                           height=40,
                           width=250,
                           corner_radius=0,
                           border_width=3,
                           border_color='#d40707')
password_entry.place(x=1100, y=430)

#Show
def toggle_password():
    if var.get() == 1:
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

var=IntVar(value=1)
show= CTkCheckBox(win,
                  text= 'Show',
                  bg_color='lightgray',
                  font=('Arial',15),
                  checkbox_height=20,
                  checkbox_width=20,
                  corner_radius=50,
                  fg_color='#d40707',
                  hover_color='#fc0303',
                  variable= var,
                  onvalue=1,
                  offvalue=0,
                  command=toggle_password)
show.place(x=1375, y=440)

#Login Button
def login_click():
    # Connect to the database
    database = sqlite3.connect('project.db')
    cursor = database.cursor()

    cursor.execute("INSERT INTO login_information VALUES (:username, :password)",
                   {
                       'username': username_entry.get(),
                       'password': password_entry.get()
                   }
                   )
     # Commit and close connection to Database
    database.commit()
    database.close()

    username = username_entry.get()
    password = password_entry.get()
    

    # Connect to the database
    database = sqlite3.connect('project.db')
    cursor = database.cursor()

    cursor.execute("SELECT * FROM customer_information WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM owners_information WHERE username = ? AND password = ?", (username, password))
    admin = cursor.fetchone()

    database.close()
    

    if  username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif user:
        win.destroy()
        subprocess.run(['python','menu.py'])

    elif admin:
        win.destroy()
        subprocess.run(['python','orderlist.py'])

    else:
        messagebox.showerror("Error","Wrong username or password")


login_button = CTkButton(win,
                text="Login",
                font=("Arial", 35,'bold'),
                height=60,
                width=250,
                text_color='black',
                fg_color='#d40707',
                bg_color='lightgray',
                hover_color='#fc0303',
                command=login_click)
login_button.place(x=1100, y=515)

def register_click():
    win.destroy()
    subprocess.run(['python','register.py'])
register_button = CTkButton(win,
                text="Register",
                font=("Arial", 15,'bold'),
                height=30,
                width=30,
                text_color='black',
                fg_color='#d40707',
                bg_color='lightgray',
                hover_color='#fc0303',
                command=register_click)
register_button.place(x=1200, y=600)

# Commit and close connection to Database
database.commit()
database.close()


win.mainloop()