from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import subprocess

win = Tk()
win.title('Order Details')
win.geometry('600x500')
win.configure(bg='white')
logo = PhotoImage(file='instantorder_logowithoutbg.png')
win.iconphoto(True, logo)

#Back Buttom
def back_click():
    win.destroy()
    subprocess.run(['python','menu.py'])
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

#Change Password Buttom
def change_password_click():
    subprocess.run(['python','change_password.py'])
def change_passwor_on_enter(e):
    change_passwor_buttom.config(bg='#fc0303',
                  fg='black')
    
def change_passwor_on_leave(e):
    change_passwor_buttom.config(bg='#d40707',
                  fg='black')
change_passwor_buttom = Button(win,
                     text='Change Password',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=change_password_click)
change_passwor_buttom.place(x=145, y=50)

change_passwor_buttom.bind('<Enter>', change_passwor_on_enter)
change_passwor_buttom.bind('<Leave>', change_passwor_on_leave)

#Change Username Buttom
def change_username_click():
    subprocess.run(['python','change_username.py'])
def change_username_on_enter(e):
    change_username_buttom.config(bg='#fc0303',
                  fg='black')
    
def change_username_on_leave(e):
    change_username_buttom.config(bg='#d40707',
                  fg='black')
change_username_buttom = Button(win,
                     text='Change Username',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=change_username_click)
change_username_buttom.place(x=140, y=200)

change_username_buttom.bind('<Enter>', change_username_on_enter)
change_username_buttom.bind('<Leave>', change_username_on_leave)

#Change Delete Buttom
def delete_click():
    subprocess.run(['python','delete.py'])

def delete_account_on_enter(e):
    delete_account_buttom.config(bg='#fc0303',
                  fg='black')
    
def delete_account_on_leave(e):
    delete_account_buttom.config(bg='#d40707',
                  fg='black')
delete_account_buttom = Button(win,
                     text='Delete Account',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=delete_click)
delete_account_buttom.place(x=160, y=350)

delete_account_buttom.bind('<Enter>', delete_account_on_enter)
delete_account_buttom.bind('<Leave>', delete_account_on_leave)


mainloop()