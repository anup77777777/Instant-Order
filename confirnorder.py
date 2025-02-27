from tkinter import *
from customtkinter import *
import subprocess

#window
popup = Tk()
popup.title("Order Confirmation")
popup.geometry("400x300")
logo = PhotoImage(file='instantorder_logowithoutbg.png')
popup.iconphoto(True, logo)
popup.configure(bg="white")
        
# Center the popup
popup.transient()
popup.grab_set()
        
# Add content with animation
frame = Frame(popup, bg="white")
frame.pack(expand=True, fill="both", padx=20, pady=20)
        
# Success icon (checkmark)
check_label = Label(frame,
                             text="✓",
                             font=("Arial", 48),
                             fg="#cc0000",
                             bg="white")
check_label.pack(pady=20)
        
# Success message
msg_label = Label(frame,
                           text="Your order has been confirmed!",
                           font=("Arial", 16, "bold"),
                           fg="#cc0000",
                           bg="white")
msg_label.pack(pady=10)

#Back Buttom
def ok_click():
    popup.destroy()
    
ok_button = CTkButton(popup,
                text="OK",
                font=("Arial", 20,'bold'),
                corner_radius=500,
                height=50,
                width=50,
                text_color='black',
                fg_color='#d40707',
                bg_color='white',
                hover_color='#fc0303',
                command=ok_click)
ok_button.place(x=175, y=225)

mainloop()