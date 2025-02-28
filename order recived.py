from tkinter import *
popup = Tk()
popup.title("Order Recived")
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
                           text="This order has been recived!",
                           font=("Arial", 16, "bold"),
                           fg="#cc0000",
                           bg="white")
msg_label.pack(pady=10)

mainloop()