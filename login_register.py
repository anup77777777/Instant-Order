from customtkinter import *
from tkinter import *
from PIL import ImageTk, Image
import subprocess

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
frame= CTkFrame(win, fg_color='lightgray', width=600, height=400, corner_radius=15)
frame.place(x=900, y=250)

#Login Button
def login_click():
    win.destroy()
    subprocess.run(['python','login.py'])
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
login_button.place(x=1080, y=300)

#Text
text1= CTkLabel(win, text="Don't have an account? You can register using the button bellow.",
                font=("Arial", 15, "bold"),
                text_color='black',
                bg_color='lightgray')
text1.place(x=970, y=390)

#Register Button
def register_click():
    win.destroy()
    subprocess.run(['python','register.py'])
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
register_button.place(x=1080, y=500)


win.mainloop()