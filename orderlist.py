from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3

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
                  text='Orders', 
                     font=('Goudy Old Style', 40, 'bold'),
                     bg='#d40707',
                     fg='white',
                     padx=463)
order_details.place(x=200, y=100)

# Order list frame inside the red rectangle
list_frame = Frame(root3, bg='white')
list_frame.place(x=210, y=190, width=1080, height=480)

# Fetch orders data from the database
conn = sqlite3.connect('orders.db')
c = conn.cursor()
c.execute("SELECT DISTINCT table_number FROM orders")
orders = c.fetchall()
conn.close()

# Create rows for each order
for order in orders:
    table_number = order[0]
    row_frame = Frame(list_frame, bg='white')
    row_frame.pack(fill='x', pady=4)  # Fill horizontal space
    
    # Order information label (left-aligned)
    info_label = Label(row_frame, 
                       text=f"Table Number: {table_number}", 
                       font=('Arial', 18), 
                       bg='white',
                       anchor='w')
    info_label.pack(side='left', anchor='w')  # Pack to the left
    
    # Open button (right-aligned)
    def open_click(table_number=table_number):
        subprocess.run(['python', 'Order.py', table_number])
    
    def delete_click(table_number=table_number):
        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        c.execute("DELETE FROM orders WHERE table_number=?", (table_number,))
        conn.commit()
        conn.close()
        row_frame.destroy()  # Remove the row from the UI

    open_btn = Button(row_frame,
                      text="Open",
                      font=('Arial', 16),
                      bg='#d40707',
                      fg='black',
                      activebackground='#fc0303',
                      activeforeground='black',
                      padx=20,
                      command=open_click)
    open_btn.pack(side='right')  # Pack to the right

    delete_btn = Button(row_frame,
                        text="Delete",
                        font=('Arial', 16),
                        bg='#d40707',
                        fg='black',
                        activebackground='#fc0303',
                        activeforeground='black',
                        padx=20,
                        command=delete_click)
    delete_btn.pack(side='right', padx=10)  # Pack to the right with padding
    
    # Hover effects
    open_btn.bind('<Enter>', lambda e, btn=open_btn: btn.config(bg='#fc0303'))
    open_btn.bind('<Leave>', lambda e, btn=open_btn: btn.config(bg='#d40707'))

root3.mainloop()