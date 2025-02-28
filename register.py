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

#Owner Button
def owner_click():
    win.destroy()
    subprocess.run(['python','owner_register.py'])
owner_button = CTkButton(win,
                text="As Owner",
                font=("Arial", 35,'bold'),
                height=60,
                width=250,
                text_color='black',
                fg_color='#d40707',
                bg_color='lightgray',
                hover_color='#fc0303',
                command=owner_click)
owner_button.place(x=1080, y=330)

#Customer Button
def customer_click():
    win.destroy()
    subprocess.run(['python','customer_register.py'])
customer_button = CTkButton(win,
                text="As Customer",
                font=("Arial", 35,'bold'),
                height=60,
                width=250,
                text_color='black',
                fg_color='#d40707',
                bg_color='lightgray',
                hover_color='#fc0303',
                command=customer_click)
customer_button.place(x=1080, y=470)



win.mainloop()