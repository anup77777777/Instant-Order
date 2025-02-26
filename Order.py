from tkinter import *
from PIL import ImageTk, Image

# Creating the main window
root3 = Tk()
root3.title('Order Details')
root3.geometry('1920x1080')
root3.configure(bg='white')

# Setting the icon
logo = PhotoImage(file='instantorder_logowithoutbg.png')
root3.iconphoto(True, logo)

# Creating a canvas
canvas = Canvas(root3, width=1920, height=1080, bg='white')
canvas.pack()
canvas.create_rectangle(200, 180, 1300, 680, outline='#d40707', width=5)

# Loading and displaying images
logo_image = PhotoImage(file='instantorder_logo.png')
original_logo_mark = Image.open('instantorder_logo.png')
resized_logo_mark = original_logo_mark.resize((120, 120), Image.Resampling.LANCZOS)
logo_mark = ImageTk.PhotoImage(resized_logo_mark)
logo_mark_label = Label(root3, image=logo_mark, bg='white')
logo_mark_label.place(x=0, y=-25)

# Creating labels
order_details = Label(root3, 
                  text='Order', 
                     font=('Goudy Old Style', 40, 'bold'),
                     bg='#d40707',
                     fg='white',
                     padx=250)
order_details.place(x=450, y=100)

# Adding "Total :" label
total_label = Label(root3, 
                    text='Total :', 
                    font=('Arial', 26, 'bold'),
                    bg='white',
                    fg='black')
total_label.place(x=1000, y=600)

# Creating buttons
next_button = Button(root3,
                     text='Back',
                     font=('Arial', 26, 'bold'),
                     bg='#d40707',
                     fg='black',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=4)
next_button.place(x=600, y=790)

# Adding event bindings
def next_on_enter(e):
    next_button.config(fg='black', bg='#fc0303')

next_button.bind('<Enter>', next_on_enter)

def next_on_leave(e):
    next_button.config(fg='black', bg='#d40707')

next_button.bind('<Leave>', next_on_leave)


# Running the main loop
root3.mainloop()
