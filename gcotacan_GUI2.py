import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import gcotacan_GUI3


def show_pay_window(email):
    pay_window = tk.Toplevel()
    pay_window.title("Payment")
    pay_window.configure(background='black')

    # Set the font
    font_style = ("Times New Roman", 12, "bold")

    # Create a ttk style with the desired font
    style = ttk.Style()
    style.configure('TButton', font=font_style)

    # Load and resize the image
    image = Image.open("Target_Logo_White.jpg")
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)

    # Create a label with the image
    image_label = tk.Label(pay_window, image=photo, bg='black')
    image_label.pack(pady=10)

    # Payment method dropdown
    payment_label = ttk.Label(pay_window, text="Select Payment Method:", background="black", foreground="red",
                              font=font_style)
    payment_label.pack(pady=5)

    payment_var = tk.StringVar()
    payment_options = ["Credit Card", "Debit Card", "PayPal", "Other"]

    payment_dropdown = ttk.Combobox(pay_window, textvariable=payment_var, values=payment_options, font=font_style,
                                    state="readonly")
    payment_dropdown.pack(pady=5)
    payment_dropdown.current(0)

    # Item categories selection
    categories_label = ttk.Label(pay_window, text="Select Item Categories:", background="black", foreground="red",
                                 font=font_style)
    categories_label.pack(pady=5)

    categories_var = []
    categories_options = ["electronics", "personal hygiene", "pet care", "grocery", "clothing", "arts & crafts", "toys"]

    for category in categories_options:
        var = tk.BooleanVar()
        cb = ttk.Checkbutton(pay_window, text=category, variable=var, onvalue=True, offvalue=False)
        cb.pack(anchor=tk.W, pady=2)
        categories_var.append((category, var))

    # Pay button
    def pay():
        payment_method = payment_var.get()
        selected_categories = [category for category, var in categories_var if var.get()]

        pay_window.destroy()
        gcotacan_GUI3.show_checkout_window(email, payment_method, selected_categories)

    pay_button = ttk.Button(pay_window, text="Pay", command=pay, style='TButton')
    pay_button.pack(pady=10)

    # Exit button
    def exit_app():
        pay_window.destroy()

    exit_button = ttk.Button(pay_window, text="Exit", command=exit_app, style='TButton')
    exit_button.pack(pady=10)

    # Run the tkinter event loop
    pay_window.mainloop()



