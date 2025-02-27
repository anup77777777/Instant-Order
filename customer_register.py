from customtkinter import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import sqlite3

# Connect to the database
database = sqlite3.connect('project.db')
cursor = database.cursor()

#Windows
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
frame= CTkFrame(win, fg_color='lightgray', width=600, height=600, corner_radius=15)
frame.place(x=900, y=110)

#Owner name
fullname=CTkLabel(win,
                text="Full Name:",
                bg_color='lightgray',
                font=("Arial", 30, 'bold'),
                text_color= 'black')
fullname.place(x=940, y=175)
fullname_entry = CTkEntry(win,
                           font=("Arial", 25,),
                           bg_color='lightgray',
                           height=40,
                           width=250,
                           corner_radius=0,
                           border_width=3,
                           border_color='#d40707')
fullname_entry.place(x=1200, y=175)

#Owner Number
number=CTkLabel(win,
                text="Number:",
                bg_color='lightgray',
                font=("Arial", 30,'bold'),
                text_color= 'black')
number.place(x=940, y=275)

def number():
    input= number_entry.get()
    if len(input)==10 and input.isdigit():
        return True
    else:
        messagebox.showerror("Error","Phone number should be 10 numbers only")
        return False
number_entry = Entry(win,
                           font=('Arial', 25),
                                 width=17,
                                 highlightthickness=4,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707',
                                 validatecommand=number,
                                 validate='focusout')
number_entry.place(x=1500, y=340)
#Username
username=CTkLabel(win,
                text="Username:",
                bg_color='lightgray',
                font=("Arial", 30,'bold'),
                text_color= 'black')
username.place(x=940, y=375)
username_entry = CTkEntry(win,
                           font=("Arial", 25,),
                           bg_color='lightgray',
                           height=40,
                           width=250,
                           corner_radius=0,
                           border_width=3,
                           border_color='#d40707')
username_entry.place(x=1200, y=375)

#Password
password=CTkLabel(win,
                text="Password:",
                font=("Arial", 30,'bold'),
                bg_color='lightgray',
                text_color= 'black')
password.place(x=940, y=475)
password_entry = CTkEntry(win,
                           font=("Arial", 25,),
                           bg_color='lightgray',
                           height=40,
                           width=250,
                           corner_radius=0,
                           border_width=3,
                           border_color='#d40707')
password_entry.place(x=1200, y=475)

#Register Button
def register_click():
    # Connect to the database
     database = sqlite3.connect('project.db')
     cursor = database.cursor()
     cursor.execute("INSERT INTO customer_information VALUES (:full_name, :number, :username, :password)",
                   {
                       'full_name': fullname_entry.get(),
                       'number': number_entry.get(),
                       'username': username_entry.get(),
                       'password': password_entry.get()
                   }
                   )


     # Commit and close connection to Database
     database.commit()
     database.close()


     if fullname_entry.get()=='' or number_entry.get()=='' or username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror("Error","All fields are required")
     else:

        win.destroy()
        subprocess.run(['python','login.py'])
register_button = CTkButton(win,
                text="Register",
                font=("Arial", 35,'bold'),
                height=60,
                width=250,
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