#Gerardo Cota Canez, CIS 345, Online Session B, Final Project Program
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import gcotacan_GUI2
from ClassFile import User  # Import the User class from ClassFile


# Function to display the sign-up window
def show_signup_window():
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.configure(background='black')

    # Set the font
    font_style = ("Times New Roman", 12, "bold")

    # Creating a ttk style with the desired font
    style = ttk.Style()
    style.configure('TButton', font=font_style)

    # Email and Password entry widgets for sign-up
    signup_email_label = tk.Label(signup_window, text="Email/Phone:", bg='black', fg='white', font=font_style)
    signup_email_label.pack(pady=5)

    signup_email_entry = ttk.Entry(signup_window, font=font_style)
    signup_email_entry.pack(pady=5)

    signup_password_label = tk.Label(signup_window, text="Password (min 9 characters):", bg='black', fg='white',
                                     font=font_style)
    signup_password_label.pack(pady=5)

    signup_password_entry = ttk.Entry(signup_window, show="*", font=font_style)
    signup_password_entry.pack(pady=5)

    # Function to create an account
    def create_account():
        email = signup_email_entry.get()
        password = signup_password_entry.get()

        if len(password) < 9:
            print("Password must be at least 9 characters long.")
            return

        if not os.path.exists("user_credentials.csv"):
            with open("user_credentials.csv", "w") as file:
                file.write("Email,Password\n")

        with open("user_credentials.csv", "a") as file:
            file.write(f"{email},{password}\n")

        signup_email_entry.delete(0, tk.END)
        signup_password_entry.delete(0, tk.END)
        print("Account created successfully!")
        signup_window.destroy()

    # Sign up button
    signup_button = ttk.Button(signup_window, text="Sign Up", command=create_account, style='TButton')
    signup_button.pack(pady=10)


# Initialize tkinter window for login
root_login = tk.Tk()
root_login.title("Target Login")
root_login.configure(background='black')

# Set the font
font_style = ("Times New Roman", 12, "bold")

# Create a ttk style with the desired font
style = ttk.Style()
style.configure('TButton', font=font_style)

# Load and resize the image
image = Image.open("Target_Logo_White.jpg")
image = image.resize((150, 150))
photo = ImageTk.PhotoImage(image)

# Creating a label with the image
image_label = tk.Label(root_login, image=photo, bg='black')
image_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Email and Password entry widgets
email_label = tk.Label(root_login, text="Email/Phone:", bg='black', fg='white', font=font_style)
email_label.grid(row=1, column=0, padx=20, pady=5, sticky=tk.E)
email_entry = ttk.Entry(root_login, font=font_style)
email_entry.grid(row=1, column=1, padx=20, pady=5)

password_label = tk.Label(root_login, text="Password:", bg='black', fg='white', font=font_style)
password_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.E)
password_entry = ttk.Entry(root_login, show="*", font=font_style)
password_entry.grid(row=2, column=1, padx=20, pady=5)

# Sign up option
signup_button = ttk.Button(root_login, text="Sign Up", command=show_signup_window, style='TButton')
signup_button.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)

# Login button
def login():
    email = email_entry.get()
    password = password_entry.get()

    # Creating a User object with values for username and user_id
    user = User(1, "", password, email)
    if user.login(password):  # Pass the input password to the login method
        print("Login successful!")
        root_login.destroy()
        gcotacan_GUI2.show_pay_window(email)
    else:
        print("Invalid email or password")


login_button = ttk.Button(root_login, text="Login", command=login, style='TButton')
login_button.grid(row=3, column=1, padx=20, pady=10, sticky=tk.E)

# Exit button
def exit_app():
    root_login.destroy()


exit_button = ttk.Button(root_login, text="Exit", command=exit_app, style='TButton')
exit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the tkinter event loop for login
root_login.mainloop()



