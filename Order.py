from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3
import sys

# Get the table number from the command line arguments
table_number = sys.argv[1]

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
                  text='Order Details', 
                     font=('Goudy Old Style', 40, 'bold'),
                     bg='#d40707',
                     fg='white',
                     padx=383)
order_details.place(x=200, y=100)

# Order details frame inside the red rectangle
details_frame = Frame(root3, bg='white')
details_frame.place(x=210, y=190, width=1080, height=480)

# Connect to the database and fetch order details
conn = sqlite3.connect('orders.db')
c = conn.cursor()
c.execute("SELECT item_name, item_count, item_price, total_price FROM orders WHERE table_number=?", (table_number,))
orders = c.fetchall()
conn.close()

# Display order details
y_position = 0
total_price = 0
# Adding a scrollbar to the details frame
scrollbar = Scrollbar(details_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Creating a canvas inside the details frame
details_canvas = Canvas(details_frame, bg='white', yscrollcommand=scrollbar.set)
details_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configuring the scrollbar
scrollbar.config(command=details_canvas.yview)

# Creating a frame inside the canvas
inner_frame = Frame(details_canvas, bg='white')
details_canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Function to update the scroll region
def update_scroll_region(event):
    details_canvas.config(scrollregion=details_canvas.bbox("all"))

inner_frame.bind("<Configure>", update_scroll_region)

# Adding mouse scroll functionality
def on_mouse_wheel(event):
    details_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

details_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Display order details
for order in orders:
    item_name, item_count, item_price, _ = order
    item_total = item_count * item_price
    total_price += item_total
    details = f" Items        : {item_name}\n Quantity   : {item_count}\n Price        : Rs. {item_price}\n"
    details_label = Label(inner_frame, text=details, font=('Arial', 18), bg='white', anchor='w', justify=LEFT)
    details_label.pack(fill='x', pady=10)
    y_position += 40

total_label = Label(root3, 
                    text=f'Total: Rs. {total_price}', 
                    font=('Arial', 26, 'bold'),
                    bg='white',
                    fg='black')
total_label.place(x=1000, y=600)



# Creating buttons
def recieve_click():
    root3.destroy()
    subprocess.run(['python','order recived.py'])
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE table_number=?", (table_number,))
    conn.commit()
    conn.close()
    



recieve_button = Button(root3,
                     text='Receive',
                     font=('Arial', 26, 'bold'),
                     bg='#d40707',
                     fg='black',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=4,
                     command=recieve_click)
recieve_button.place(x=600, y=700)

# Adding event bindings
def recieve_on_enter(e):
    recieve_button.config(fg='black', bg='#fc0303')

recieve_button.bind('<Enter>', recieve_on_enter)

def recieve_on_leave(e):
    recieve_button.config(fg='black', bg='#d40707')

recieve_button.bind('<Leave>', recieve_on_leave)

# Adding a new button on the left side at the bottom
def back_click():
    root3.destroy()

back_button = Button(root3,
                     text='Back',
                     font=('Arial', 20, 'bold'),
                     bg='#d40707',
                     fg='black',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=10,
                     pady=0,
                     command=back_click)
back_button.place(x=50, y=710)

# Running the main loop
root3.mainloop()
