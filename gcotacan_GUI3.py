import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json


def show_checkout_window(email, payment_method, selected_categories):
    checkout_window = tk.Toplevel()
    checkout_window.title("Checkout")
    checkout_window.configure(background='black')

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
    image_label = tk.Label(checkout_window, image=photo, bg='black')
    image_label.pack(pady=10)

    # Search bar for "Type Item(s)"
    search_label = ttk.Label(checkout_window, text="Type Item(s):", background="black", foreground="red",
                             font=font_style)
    search_label.pack(pady=5)

    search_var = tk.StringVar()
    search_entry = ttk.Entry(checkout_window, textvariable=search_var, font=font_style)
    search_entry.pack(pady=5)

    # Add and Delete buttons
    def add_item():
        item = search_var.get()

        print(f"Added item: {item}")

    add_button = ttk.Button(checkout_window, text="Add", command=add_item, style='TButton')
    add_button.pack(pady=10)

    # Category selection
    categories_label = ttk.Label(checkout_window, text="Continue Shopping:", background="black", foreground="red",
                                 font=font_style)
    categories_label.pack(pady=5)

    categories_var = []

    categories_options = ["electronics", "personal hygiene", "pet care", "grocery", "clothing", "arts & crafts", "toys"]
    for category in categories_options:
        var = tk.BooleanVar()
        categories_var.append((category, var))
        chk = ttk.Checkbutton(checkout_window, text=category, variable=var, onvalue=True, offvalue=False)
        chk.pack(pady=5)

    def delete_item():
        item = search_var.get()
        selected_categories = [category[0] for category, var in categories_var if var.get()]
        # Implementing logic for deleting the item from the list and json file

        if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
            with open('data.json', 'r') as file:
                data = json.load(file)
        else:
            data = []

        new_data = [entry for entry in data if entry["user"] != email or entry["categories"] not in selected_categories or entry["item"] != item]

        with open('data.json', 'w') as file:
            json.dump(new_data, file, indent=4)

        print(f"Deleted item: {item}")

    delete_button = ttk.Button(checkout_window, text="Delete", command=delete_item, style='TButton')
    delete_button.pack(pady=10)

    # Confirm and total display
    def confirm():
        total = 0  # Placeholder for total amount
        # Calculate a total based on the category
        if selected_categories:
            total += len(selected_categories) * 10  # Assuming $10 per category

        message = f"Thank you {email} your total is ${total}."
        # Display the message
        confirmation_label.config(text=message, foreground='red')

        # Save data to JSON file
        new_entry = {
            "user": email,
            "categories": selected_categories,
            "payment_method": payment_method,
            "total": total
        }

        if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
            with open('data.json', 'r') as file:
                data = json.load(file)
        else:
            data = []

        data.append(new_entry)

        # Write data back to the JSON file
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

    confirm_button = ttk.Button(checkout_window, text="Confirm", command=confirm, style='TButton')
    confirm_button.pack(pady=10)

    confirmation_label = ttk.Label(checkout_window, text="", background="black", foreground="white", font=font_style)
    confirmation_label.pack(pady=5)

    # Exit button
    def exit_app():
        checkout_window.destroy()

    exit_button = ttk.Button(checkout_window, text="Exit", command=exit_app, style='TButton')
    exit_button.pack(pady=10)

    # Run the tkinter event loop
    checkout_window.mainloop()
