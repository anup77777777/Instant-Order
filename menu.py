from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
import sqlite3

# Global variable to store table number
table_number = ""

def placeorder_click():
    global table_number
    milk_tea_count= int(milk_tea_sb.get())
    black_tea_count= int(black_tea_sb.get())
    hot_lemon_count= int(hot_lemon_sb.get())
    black_coffee_count= int(black_coffee_sb.get())
    milk_coffee_count= int(milk_coffee_sb.get())
    hot_chocolate_count= int(hot_chocolate_sb.get())
    coke_count=int(coke_sb.get())
    sprite_count=int(sprite_sb.get())
    fanta_count=int(fanta_sb.get())
    lassi_count=int(lassi_sb.get())
    veg_momo_count=int(veg_momo_sb.get())
    buff_momo_count=int(buff_momo_sb.get())
    chicken_momo_count=int(chicken_momo_sb.get())
    chicken_burger_count=int(chicken_burger_sb.get())
    ham_burger_count=int(ham_burger_sb.get())
    veg_burger_count=int(veg_burger_sb.get())
    chicken_pizza_count=int(chicken_pizza_sb.get())
    mushroom_pizza_count=int(mushroom_pizza_sb.get())
    cheese_pizza_count=int(cheese_pizza_sb.get())

    selected_items=sum(1 for count in [milk_tea_count, 
                                       black_tea_count, 
                                       hot_lemon_count, 
                                       black_coffee_count, 
                                       milk_coffee_count, 
                                       hot_chocolate_count, 
                                       coke_count, sprite_count, 
                                       fanta_count, 
                                       lassi_count, 
                                       veg_momo_count, 
                                       buff_momo_count, 
                                       chicken_momo_count, 
                                       chicken_burger_count, 
                                       ham_burger_count, 
                                       veg_burger_count, 
                                       chicken_pizza_count, 
                                       mushroom_pizza_count, 
                                       cheese_pizza_count] if count > 0)
    if selected_items >= 1:
        def next_on_enter(e):
            next_button.config(fg='black',
                       bg='#fc0303')

        def next_on_leave(e):
            next_button.config(fg='black',
                       bg='#d40707')

        #window
        root1 = Toplevel(root)
        root1.title('Table Number')
        root1.geometry('1920x1080')
        root1.configure(bg='white')
        logo = PhotoImage(file='instantorder_logowithoutbg.png')
        root1.iconphoto(True, logo)

        #Canvas
        canvas = Canvas(root1, width=1920, height=1080, bg='white')
        canvas.pack()
        canvas.create_rectangle(300, 100, 1200, 600, outline='#d40707', width=5)
        
        #Logo Mark
        logo_image= PhotoImage(file='instantorder_logo.png')
        original_logo_mark = Image.open('instantorder_logo.png')
        resized_logo_mark = original_logo_mark.resize((120, 120), Image.Resampling.LANCZOS)
        logo_mark= ImageTk.PhotoImage(resized_logo_mark)
        logo_mark_label = Label(root1, image = logo_mark, bg='white')
        logo_mark_label.place(x=0, y=-25)

        #Insert Your Table Number
        insert_your_table_number = Label(root1, 
                     text='Insert Your Table Number', 
                     font=('Goudy Old Style', 40, 'bold'),
                     bg='#d40707',
                     fg='white',
                     padx=100)
        insert_your_table_number.place(x=330, y=120)

            
        table_number_entry = Entry(root1,
                                 font=('Arial', 70),
                                 justify='center',
                                 width=10,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
        table_number_entry.place(x=460, y=330)
        def next_click():
            if len(table_number_entry.get())==0:
                messagebox.showerror("Error","Table number cannot be empty.")

            elif len(table_number_entry.get())<4:
                global table_number
                table_number = table_number_entry.get()
                root1.destroy()

                def confirm_on_enter(e):
                    confirm_button.config(fg='black',
                                          bg='#fc0303')

                def confirm_on_leave(e):
                    confirm_button.config(fg='black',
                                           bg='#d40707')
                
                def back_on_enter(e):
                    back_button.config(fg='black',
                                          bg='#fc0303')

                def back_on_leave(e):
                    back_button.config(fg='black',
                                           bg='#d40707')
            
                # Calculate total prices
                items = [
                    ("Milk Tea", milk_tea_count, 25),
                    ("Black Tea", black_tea_count, 20),
                    ("Hot Lemon", hot_lemon_count, 30),
                    ("Black Coffee", black_coffee_count, 40),
                    ("Milk Coffee", milk_coffee_count, 50),
                    ("Hot Chocolate", hot_chocolate_count, 90),
                    ("Coke", coke_count, 60),
                    ("Sprite", sprite_count, 60),
                    ("Fanta", fanta_count, 60),
                    ("Lassi", lassi_count, 60),
                    ("Veg MoMo", veg_momo_count, 100),
                    ("Buff MoMo", buff_momo_count, 130),
                    ("Chicken MoMo", chicken_momo_count, 150),
                    ("Chicken Burger", chicken_burger_count, 310),
                    ("Ham Burger", ham_burger_count, 280),
                    ("Veg Burger", veg_burger_count, 230),
                    ("Chicken Pizza", chicken_pizza_count, 550),
                    ("Mushroom Pizza", mushroom_pizza_count, 450),
                    ("Cheese Pizza", cheese_pizza_count, 500)
                ]

                total_price = 0 #total price of all items
                y_position = 230 #position of the first item

                #window
                root2= Toplevel()
                root2.geometry('1920x1080')
                root2.title('Confirm Order')
                root2.configure(bg='white')
                logo = PhotoImage(file='instantorder_logowithoutbg.png')

                #Canvas
                canvas = Canvas(root2, width=1920, height=1080, bg='white')
                canvas.pack()
                canvas.create_rectangle(200, 180, 1300, 680, outline='#d40707', width=5)

                #Your Order
                your_order= Label(root2,
                              text='Your Order',
                              font=('Goudy Old Style', 40, 'bold'),
                              fg='white',
                              bg='#d40707',
                              padx=300)
                your_order.place(x=320, y=100)

                # Display table number
                table_number_label = Label(root2, text=f"Table Number : {table_number}",
                                       font=('Arial', 18, ), 
                                       fg='black', 
                                       bg='white')
                table_number_label.place(x=250, y=200)

                # Display items and their total prices
                for item_name, item_count, item_price in items:
                    if item_count > 0:
                        item_total_price = item_count * item_price
                        total_price += item_total_price
                        item_label = Label(root2,
                                       text=f"{item_name} : {item_count} x Rs. {item_price}",
                                       font=('Arial', 18), 
                                       fg='black', 
                                       bg='white')
                        item_label.place(x=250, y=y_position)
                        y_position += 40

                # Overall total price
                total_price_label = Label(root2, text=f"Total : Rs. {total_price}", 
                                      font=('Arial', 25, 'bold')
                                      , fg='#d40707', 
                                      bg='white')
                total_price_label.place(x=660, y=620)

                #Confirm
                def confirm_click():
                    # Save order data to database
                    conn = sqlite3.connect('orders.db')
                    c = conn.cursor()
                    c.execute('''CREATE TABLE IF NOT EXISTS orders
                             (table_number TEXT, item_name TEXT, item_count INTEGER, item_price INTEGER, total_price INTEGER)''')
                
                    for item_name, item_count, item_price in items:
                        if item_count > 0:
                            item_total_price = item_count * item_price
                            c.execute("INSERT INTO orders (table_number, item_name, item_count, item_price, total_price) VALUES (?, ?, ?, ?, ?)",
                                      (table_number, item_name, item_count, item_price, item_total_price))
                
                    conn.commit()
                    conn.close()
                    root.destroy()
                    subprocess.run(['python', 'confirnorder.py'])
                    
            else:
                messagebox.showerror("Error","Table number can only be 3 characters.")
                

            confirm_button=Button(root2,
                                  text='Confirm',
                                  font=('Arial', 28, 'bold'),
                                  fg='Black',
                                  bg='#d40707',
                                  activeforeground='black',
                                  activebackground='#fc0303',
                                  padx=30,
                                  pady=0,
                                  command=confirm_click)
            confirm_button.place(x=680, y= 700)
            confirm_button.bind('<Enter>', confirm_on_enter)
            confirm_button.bind('<Leave>', confirm_on_leave)

            def back_click():
                root2.destroy()

            #Back Button
            back_button=Button(root2,
                                  text='Back To Menu',
                                  font=('Arial', 15, 'bold'),
                                  fg='Black',
                                  bg='#d40707',
                                  activeforeground='black',
                                  activebackground='#fc0303',
                                  command=back_click,
                                  padx=0,
                                  pady=0)
            back_button.place(x=100, y= 722)
            back_button.bind('<Enter>', back_on_enter)
            back_button.bind('<Leave>', back_on_leave)


        #Next Button
        next_button = Button(root1,
                     text='Next',
                     font=('Arial', 28, 'bold'),
                     bg='#d40707',
                     fg='black',
                     activeforeground='black',
                     activebackground='#fc0303',
                     command= next_click,

                     padx=80,
                     pady=-0,)
        next_button.place(x=1070, y=650)
        next_button.bind('<Enter>',next_on_enter)
        next_button.bind('<Leave>',next_on_leave)

    else:
        messagebox.showerror('Error', 'Please selected at least one item form menu.')
def placeorder_on_enter(e):
    place_order.config(bg='#fc0303',
                  fg='black')
    
def placeorder_on_leave(e):
    place_order.config(bg='#d40707',
                  fg='black')

#window
root = Tk()
root.title('Instant Order')
root.geometry('1920x1080')
root.config(bg='white')
logo = PhotoImage(file='instantorder_logowithoutbg.png')
root.iconphoto(True, logo)

#Border
canvas = Canvas(root, width=1920, height=1080, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_rectangle(20, 100, 1510, 700, outline='#d40707', width=5, dash=(5,2))

#Logo Mark
logo_image= PhotoImage(file='instantorder_logo.png')
original_logo_mark = Image.open('instantorder_logo.png')
resized_logo_mark = original_logo_mark.resize((120, 120), Image.Resampling.LANCZOS)
logo_mark= ImageTk.PhotoImage(resized_logo_mark)
logo_mark_label = Label(root, image = logo_mark, bg='white')
logo_mark_label.place(x=0, y=-25)

#Menu
menu= Label(root,
            text='MENU',
            font=('Goudy Old Style', 35, 'bold'),
             fg='white',
             bg='#d40707',
             padx=600,
             pady=0)
menu.place(x=95, y=120)

#Hot Drinks
hot_drinks = Label(root,
                   text='Hot Drinks',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
hot_drinks.place(x=190, y=200)

#milk tea
milk_tea= Label(root,
                text='Milk Tea..................',
                font=('Arial', 18),
                fg='black',
                bg='white')
milk_tea.place(x=190, y=240)

milk_tea_price= Label(root,
                text='Rs. 25',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
milk_tea_price.place(x=410, y=240)

milk_tea_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
milk_tea_sb.place(x=500, y=245)

#black tea
black_tea= Label(root,
                text='Black Tea................',
                font=('Arial', 18),
                fg='black',
                bg='white')
black_tea.place(x=190, y=280)

black_tea_price= Label(root,
                text='Rs. 20',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
black_tea_price.place(x=410, y=280)

black_tea_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
black_tea_sb.place(x=500, y=285)

#hot  lemon
hot_lemon= Label(root,
                text='Hot Lemon...............',
                font=('Arial', 18),
                fg='black',
                bg='white')
hot_lemon.place(x=190, y=320)

hot_lemon_price= Label(root,
                text='Rs. 30',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
hot_lemon_price.place(x=410, y=320)

hot_lemon_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
hot_lemon_sb.place(x=500, y=325)

#black coffee
black_coffee= Label(root,
                text='Black Coffee............',
                font=('Arial', 18),
                fg='black',
                bg='white')
black_coffee.place(x=190, y=360)

black_coffee_price= Label(root,
                text='Rs. 40',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
black_coffee_price.place(x=410, y=360)

black_coffee_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
black_coffee_sb.place(x=500, y=365)

#milk coffee
milk_coffee= Label(root,
                text='Milk Coffee...............',
                font=('Arial', 18),
                fg='black',
                bg='white')
milk_coffee.place(x=190, y=400)

milk_coffe_price= Label(root,
                text='Rs. 50',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
milk_coffe_price.place(x=410, y=400)

milk_coffee_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
milk_coffee_sb.place(x=500, y=405)

#hot chocolate
hot_chocolate= Label(root,
                text='Hot Chocolate..........',
                font=('Arial', 18),
                fg='black',
                bg='white')
hot_chocolate.place(x=190, y=440)

hot_chocolate_price= Label(root,
                text='Rs. 90',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
hot_chocolate_price.place(x=410, y=440)

hot_chocolate_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
hot_chocolate_sb.place(x=500, y=445)

#Cold Drinks
cold_drinks = Label(root,
                   text='Cold Drinks',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
cold_drinks.place(x=190, y=500)

#coke
coke= Label(root,
                text='Coke......................',
                font=('Arial', 18),
                fg='black',
                bg='white')
coke.place(x=190, y=540)

coke_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
coke_price.place(x=410, y=540)

coke_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
coke_sb.place(x=500, y=545)

#sprite
sprite= Label(root,
                text='Sprite.....................',
                font=('Arial', 18),
                fg='black',
                bg='white')
sprite.place(x=190, y=580)

sprite_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
sprite_price.place(x=410, y=580)

sprite_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
sprite_sb.place(x=500, y=585)

#fanta
fanta= Label(root,
                text='Fanta.....................',
                font=('Arial', 18),
                fg='black',
                bg='white')
fanta.place(x=190, y=620)

fanta_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
fanta_price.place(x=410, y=620)

fanta_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
fanta_sb.place(x=500, y=625)

#lassi
lassi= Label(root,
                text='Lassi......................',
                font=('Arial', 18),
                fg='black',
                bg='white')
lassi.place(x=190, y=660)

lassi_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
lassi_price.place(x=410, y=660)

lassi_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
lassi_sb.place(x=500, y=665)

#MoMo
momo = Label(root,
                   text='MoMo',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
momo.place(x=900, y=200)

#veg momo
veg_momo= Label(root,
                text='Veg MoMo..................',
                font=('Arial', 18),
                fg='black',
                bg='white')
veg_momo.place(x=900, y=240)

veg_momo_price= Label(root,
                text='Rs. 100',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
veg_momo_price.place(x=1140, y=240)

veg_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
veg_momo_sb.place(x=1250, y=245)

#buff momo
buff_momo= Label(root,
                text='Buff MoMo.................',
                font=('Arial', 18),
                fg='black',
                bg='white')
buff_momo.place(x=900, y=280)

buff_momo_price= Label(root,
                text='Rs. 130',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
buff_momo_price.place(x=1140, y=280)

buff_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
buff_momo_sb.place(x=1250, y=285)

#chicken momo
chicken_momo= Label(root,
                text='Chicken MoMo............',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_momo.place(x=900, y=320)

chicken_momo_price= Label(root,
                text='Rs. 150',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_momo_price.place(x=1140, y=320)

chicken_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_momo_sb.place(x=1250, y=325)

#Burger
burger = Label(root,
                   text='Burger',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
burger.place(x=900, y=370)

#chicken burger
chicken_burger= Label(root,
                text='Chicken Burger...........',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_burger.place(x=900, y=410)

chicken_burger_price= Label(root,
                text='Rs. 310',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_burger_price.place(x=1140, y=410)

chicken_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_burger_sb.place(x=1250, y=415)

#ham burger
ham_burger= Label(root,
                text='Ham Burger................',
                font=('Arial', 18),
                fg='black',
                bg='white')
ham_burger.place(x=900, y=450)

ham_burger_price= Label(root,
                text='Rs. 280',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
ham_burger_price.place(x=1140, y=450)

ham_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
ham_burger_sb.place(x=1250, y=455)

#veg burger
veg_burger= Label(root,
                text='Veg Burger................',
                font=('Arial', 18),
                fg='black',
                bg='white')
veg_burger.place(x=900, y=490)

veg_burger_price= Label(root,
                text='Rs. 230',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
veg_burger_price.place(x=1140, y=490)

veg_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
veg_burger_sb.place(x=1250, y=495)

#Pizza
pizza = Label(root,
                   text='Pizza',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
pizza.place(x=900, y=540)

#chicken pizza
chicken_pizza= Label(root,
                text='Chicken Pizza(M).........',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_pizza.place(x=900, y=580)

chicken_pizza_price= Label(root,
                text='Rs. 550',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_pizza_price.place(x=1140, y=580)

chicken_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_pizza_sb.place(x=1250, y=585)

#mushroom pizza
mushroom_pizza= Label(root,
                text='Mushroom Pizza(M)...',
                font=('Arial', 18),
                fg='black',
                bg='white')
mushroom_pizza.place(x=900, y=620)

mushroom_pizza_price= Label(root,
                text='Rs. 450',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
mushroom_pizza_price.place(x=1140, y=620)

mushroom_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
mushroom_pizza_sb.place(x=1250, y=625)

#cheese pizza
cheese_pizza= Label(root,
                text='Cheese Pizza(M).........',
                font=('Arial', 18),
                fg='black',
                bg='white')
cheese_pizza.place(x=900, y=660)

cheese_pizza_price= Label(root,
                text='Rs. 500',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
cheese_pizza_price.place(x=1140, y=660)

cheese_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
cheese_pizza_sb.place(x=1250, y=665)

#Place order
place_order = Button(root,
                     text='Place Order',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,
                     command=placeorder_click)
place_order.place(x=1276, y=720)
place_order.bind('<Enter>', placeorder_on_enter)
place_order.bind('<Leave>', placeorder_on_leave)


#Adding Profile Buttom abd bill button
def profile_click():
    root10 = Toplevel()
    root10.title('Order Details')
    root10.geometry('600x500')
    root10.configure(bg='white')
    logo = PhotoImage(file='instantorder_logowithoutbg.png')
    root10.iconphoto(True, logo)

    


    #Manage Buttom
    def manage_click():
        root10.destroy()
        root.destroy()
        subprocess.run(['python','manageAccount.py'])
        
          

    #Bill Buttom

    def bill_on_enter(e):
        bill_buttom.config(bg='#fc0303',
                  fg='black')
    
    def bill_on_leave(e):
        bill_buttom.config(bg='#d40707',
                  fg='black')
    
    bill_buttom = Button(root10,
                     text='Bill',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0,)
                     #command=bill_click)
    bill_buttom.place(x=225, y=350)

    bill_buttom.bind('<Enter>', bill_on_enter)
    bill_buttom.bind('<Leave>', bill_on_leave)

profile_button = CTkButton(canvas,
                text="≡",
                font=("Arial", 35,'bold'),
                corner_radius=500,
                height=50,
                width=50,
                text_color='black',
                fg_color='#d40707',
                bg_color='white',
                hover_color='#fc0303',
                command=profile_click)
profile_button.place(x=1450, y=10)


mainloop()