import tkinter as tk
from tkinter import messagebox
import pywinstyles
import mysql.connector
import hashlib

# Connecting to database

connection = mysql.connector.connect(host="localhost",
                                     user = "root",
                                     password = "",
                                     database = "hospital_management_syste")

cursor = connection.cursor()

# Main Window

root = tk.Tk()
root.title("Little Angels Baby Care Hospital",)
root.geometry("")
root.configure(background="#009688")

# Title

title_frame = tk.Frame(root,background="#009688")
title_frame.pack(fill='x')
title = tk.Label(title_frame, text="Little Angels Baby Care Hospital", font=("Times New Roman", 24), fg="white", bg="#009688")
title.pack(pady=20)

# Container

page_container = tk.Frame(root,background="#009688")
page_container.pack(side="top", fill="both", expand=True)

# First frame

registration_page =tk.Frame(page_container, background="#009688")
registration_page.place(relx=0.5, rely=0.5, anchor="center")

# Registration Information

name =tk.Label(registration_page, text="User name", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_name =tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14))
email = tk.Label(registration_page, text="Email address", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_email =tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14))
dob = tk.Label(registration_page, text="Date of Birth (YYYY/MM/DD)", background="#009688", fg="white", font=("Times New Roman", 18))
txt_dob = tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14))
phone_number = tk.Label(registration_page, text="Contact number", background="#009688", fg="white", font=("Times New Roman", 18))
txt_phone_number = tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14))
password = tk.Label(registration_page, text="Password", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_password = tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14), show="*")
con_password = tk.Label(registration_page, text="Re-enter password", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_con_password= tk.Entry(registration_page, width=30, fg="black", font=("Times New Roman", 14), show="*")

name.pack(pady=8)
txt_box_name.pack(pady=8, ipady=8)
email.pack(pady=8)
txt_box_email.pack(pady=8, ipady=8)
dob.pack(pady=8)
txt_dob.pack(pady=8, ipady=8)
phone_number.pack(pady=8)
txt_phone_number.pack(pady=8, ipady=8)
password.pack(pady=8)
txt_box_password.pack(pady=8, ipady=8)
con_password.pack(pady=8)
txt_box_con_password.pack(pady=8, ipady=8)

# Registration function

def register():
    name = txt_box_name.get()
    email = txt_box_email.get()
    dob = txt_dob.get()
    phone_number = txt_phone_number.get()
    password = txt_box_password.get()
    con_password = txt_box_con_password.get()

    # Checking accuracy of both entered passwords.

    if password != con_password:
        messagebox.showerror("Registration Failed! Please try again.", "Passwords do not match")

        return

    try:

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Inserting registration information to database.

        sql_insert="""INSERT into patients (name, email, dob, phone_number, password) VALUES (%s,%s,%s,%s,%s)"""

        values = (name, email, dob, phone_number, hashed_password)
        cursor.execute(sql_insert, values)

        connection.commit()

        registration_success_page.tkraise()

    except mysql.connector.Error as error_1 :
        messagebox.showerror("Registration Failed! Please try again.", str(error_1))
        # Displays error message in a dialog box


# Enable switch between pages

button_frame = tk.Frame(registration_page, bg="#009688")
button_frame.pack()

btn_register =tk.Button(button_frame, text="Register", font=("Times New Roman", 18), bg= "#00796B", fg="white", command= register)
btn_register.pack(side="left", padx=10)

def show_login_page():
    login_page.tkraise()

btn_click_to_login = tk.Button(button_frame, text="Click here to login", font=("Times New Roman", 18), fg="white", bg="#007968", command=show_login_page)
btn_click_to_login.pack(side="left", padx=10)

# Second Frame

registration_success_page = tk.Frame(page_container, background="#009688")
registration_success_page.place(relwidth=1, relheight=1)

registration_success = tk.Label(registration_success_page, text="You have successfully registered",fg="white", font=("Times New Roman", 16), bg="#00796B")
registration_success.pack(pady=10)

def show_login_page():
    login_page.tkraise()

btn_click_to_login = tk.Button(registration_success_page, text="Click here to login", font=("Times New Roman", 18), fg="white", bg="#007968", command=show_login_page)
btn_click_to_login.pack(pady=10)

# login page

login_page = tk.Frame(page_container, background="#009688")
login_page.place(relwidth=1, relheight=1)

# Login Credential

name_login_page = tk.Label(login_page, text="User name", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_name_login_page =tk.Entry(login_page, width=30, fg="black", font=("Times New Roman", 14))
password_login_page = tk.Label(login_page, text="Password", background="#009688", fg="white", font=("Times New Roman", 18))
txt_box_password_login_page = tk.Entry(login_page, width=30, fg="black", font=("Times New Roman", 14), show="*")

name_login_page.pack(pady=8)
txt_box_name_login_page.pack(pady=8, ipady=8)
password_login_page.pack(pady=8)
txt_box_password_login_page.pack(pady=8, ipady=8)

# Login functions

def login():
    name = txt_box_name_login_page.get()
    password = txt_box_password_login_page.get()

    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Checking accuracy of login credentials.

        sql_fetch = """SELECT * FROM patients WHERE name=%s AND password=%s;"""
        cursor.execute(sql_fetch, (name, hashed_password))
        results = cursor.fetchone()

        if results:
            messagebox.showinfo("Login Successful!", "Welcome to Little Angels Baby Care Hospital!")
        else:
            messagebox.showerror("Login Failed! Please try again.", "Name or Passwords incorrect")

    except mysql.connector.Error as error_1 :
        messagebox.showerror("Error connecting to database.", str(error_1))


btn_login = tk.Button(login_page, text="Login", font=("Times New Roman", 18), fg="white", bg="#007968", command=login)
btn_login.pack(pady=10)

registration_page.tkraise()

# Applying dark theme to windows background

pywinstyles.apply_style(root, "dark")
root.mainloop()