# impoting modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as Tb
from ttkbootstrap import *
from ttkbootstrap.constants import *
import csv
import ctypes
import os 
import sys
import stat
import base64
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import webbrowser

def at_first():

    main_window = Tb.Window(themename="darkly", title="TeXtCrYpTeR (Access)")
    main_window.config(bg="#222222")
    main_window.maxsize(width=550, height=345)
    main_window.minsize(width=550, height=345)

    # disableing resizable factor
    main_window.resizable(False, False)

    # launching the app at the centre  of the screen

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    app_width = 550
    app_height = 345

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    main_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # window icon
    main_window.iconbitmap(r'assets/padlock.ico')
    icon = r'assets/padlock.ico'
    main_window.iconbitmap(default=icon)

    # version

    version = tk.Label(main_window, text="Version 1.0", font=("monospace", 8, "bold"))
    version.config(bg="#222222", fg="#DF1FE3")
    version.place(x=240, y=81)

    # setting back ground image
    picpad = tk.PhotoImage(file="assets/padlock.png")
    picpad_placer = tk.Label(main_window, image=picpad, bg="#222222")
    picpad_placer.place(x=0, y=120)

    # frame of the app name

    frame = tk.PhotoImage(file="assets/textcrypter.png")
    frame_place = tk.Label(main_window, image=frame, bg="#222222")
    frame_place.place(x=165, y=20)

    # lock

    lock = tk.Label(main_window, text="●", font=("monospace", 15, "bold"))
    lock.config(fg="#ff4d4d", height=1, width=1)
    lock.place(x=68, y=210)

    # lock frame

    locked_frame = tk.Frame(main_window, width=105, bg="white", height=40)
    locked_frame.place(x=23, y=265)
    # status
    locked_place = tk.Label(locked_frame, text="STATUS :  LOCKED", font=("Arial", 8, 'bold'))
    locked_place.config(bg="#222222", fg="#FF4D4D", relief=FLAT)
    locked_place.place(x=1, y=2)

    # frame

    container = PhotoImage(file="assets/content.png")
    container_place = tk.Label(main_window, image=container)
    container_place.place(x=140, y=108)

    # user Id entry

    user_id_variable = StringVar()

    user_id_entry = tk.Entry(main_window, textvariable=user_id_variable, font=("monospace", 13, "bold"))
    user_id_entry.config(bg="white", relief=FLAT, width=26, highlightbackground="white", highlightcolor="white",highlightthickness=1, fg="gray17", insertbackground="gray")
    user_id_entry.place(x=246, y=150)

    # password_entry

    password_entry_variable = StringVar()

    password_entry = tk.Entry(main_window, textvariable=password_entry_variable, font=("monospace", 13, "bold"))
    password_entry.config(bg="white", relief=FLAT, width=19, highlightbackground="white", highlightcolor="white",
                          highlightthickness=1, fg="gray17", show="*", insertbackground="gray")
    password_entry.place(x=268, y=208)

    # create an account

    def create_account_first():

        user_id_entry.delete(0, END)
        password_entry.delete(0, END)
        main_window.withdraw()

        # launching second window

        create_account_window = tk.Toplevel()
        create_account_window.title("TeXtCrYpTeR (Create Account)")
        create_account_window.grab_set()
        create_account_window.maxsize(width=570, height=485)
        create_account_window.minsize(width=570, height=485)

        # disableing resizble factor
        create_account_window.resizable(False, False)

        # launching the app at the centre  of the screen

        screen_width = create_account_window.winfo_screenwidth()
        screen_height = create_account_window.winfo_screenheight()

        app_width = 570
        app_height = 485

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        create_account_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # version

        version = tk.Label(create_account_window, text="Version 1.0", font=("monospace", 8, "bold"))
        version.config(bg="#222222", fg="#DF1FE3")
        version.place(x=388, y=66)

        # window icon
        create_account_window.iconbitmap(r'assets/padlock.ico')
        icon = r'assets/padlock.ico'
        create_account_window.iconbitmap(default=icon)

        # texctcryptor
        img_text = Image.open("assets/textcrypter.png")
        text_image = ImageTk.PhotoImage(img_text)
        text_image_place = tk.Label(create_account_window, image=text_image)
        text_image_place.place(x=165, y=20)

        # sign up container

        container_img = Image.open("assets/sign_up.png")
        container_image = ImageTk.PhotoImage(container_img)
        container_image_place = tk.Label(create_account_window, image=container_image)
        container_image_place.place(x=50, y=90)

        # back button
        def back_button():
            create_account_window.destroy()
            main_window.deiconify()

        img_back = Image.open("assets/back.png")
        image_back = ImageTk.PhotoImage(img_back)
        image_back_place = tk.Button(create_account_window, image=image_back, command=back_button)
        image_back_place.config(bg="#222222", activebackground="#222222", relief=FLAT,cursor="hand2")
        image_back_place.place(x=52, y=40)

        # email id entry

        email_id_variable = StringVar()

        email_id_entry = tk.Entry(create_account_window, textvariable=email_id_variable,font=("monospace", 13, "bold"))
        email_id_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17", insertbackground="gray")
        email_id_entry.place(x=253, y=120)

        # user id entry

        create_user_id_variable = StringVar()

        create_user_id_entry = tk.Entry(create_account_window, textvariable=create_user_id_variable,font=("monospace", 13, "bold"))
        create_user_id_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray")
        create_user_id_entry.place(x=253, y=170)

        # password entry

        password_create_variable = StringVar()

        create_password_entry = tk.Entry(create_account_window, textvariable=password_create_variable,font=("monospace", 13, "bold"), show="*")
        create_password_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",insertbackground="gray")
        create_password_entry.place(x=253, y=220)

        # confirm password entry

        password_confirm_create_variable = StringVar()

        create_password_confirm_entry = tk.Entry(create_account_window,textvariable=password_confirm_create_variable,font=("monospace", 13, "bold"), show="*")
        create_password_confirm_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray")
        create_password_confirm_entry.place(x=253, y=270)

        # first name entry

        first_name_variable = StringVar()

        first_name_entry = tk.Entry(create_account_window, textvariable=first_name_variable,font=("monospace", 13, "bold"))
        first_name_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white", highlightcolor="white", highlightthickness=1, fg="gray17", insertbackground="gray")
        first_name_entry.place(x=253, y=317)

        # last name

        lasst_name_variable = StringVar()

        last_name_entry = tk.Entry(create_account_window, textvariable=lasst_name_variable,font=("monospace", 13, "bold"))
        last_name_entry.config(bg="white", relief=FLAT, width=25, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17", insertbackground="gray")
        last_name_entry.place(x=253, y=365)

        # main regsitering

        def register_now():

            # if emial is empty

            def message_unsuccessful_email():
                messagebox.showerror(title="ERROR", message="EMAIL CANNOT BE EMPTY")

            # if user id is blank

            def message_unsuccessful_userid():
                messagebox.showerror(title="ERROR", message="USER ID CANNOT BE EMPTY")

            # if password entry is blank

            def message_unsuccessfull_password():
                messagebox.showerror(title="ERROR", message="PASSWORD CANNOT BE EMPTY")

            # if lenth is les than 8 character
            def message_password_length_error():
                messagebox.showerror(title="ERROR", message="PASSWORD CANNOT BE MORE LESS THAN 8 CHARACTERS")

            # if confirm psasword is empty

            def message_unsuccessful_confirm_password():
                messagebox.showerror(title="ERROR", message="PLEASE CONFIRM THE PASSWORD TO CONTINUE")

            # if password doesnot match the

            def message_unsuccessful_password_missmatch():
                messagebox.showerror(title="ERROR", message="PASSWORD DID NOT MATCHED")

            # if first name is empty

            def message_unsuccessful_firtname_empty():
                messagebox.showerror(title="ERROR", message="FIRST NAME CANNOT BE EMPTY")

            # if last name is empty

            def message_unsuccesful_lastname_empty():
                messagebox.showerror(title="ERROR", message="LAST NAME CANNOT BE EMPTY")

            # when evrything is alright

            def successfull():

                # path of Textcrypter
                path_of_textcrypter = "C:/TeXtCrYpTeR"

                # if not
                if not os.path.exists(path_of_textcrypter):
                    os.mkdir(path_of_textcrypter)

                    # path of key folder
                    path_of_key_folder = "C:/TeXtCrYpTeR/key"

                    # if not

                    if not os.path.exists(path_of_key_folder):
                        os.mkdir(path_of_key_folder)

                        # path of key file
                        path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"

                        # if not

                        if not os.path.isfile(path_of_key_file):

                            # generate key file

                            key = Fernet.generate_key()
                            keyfile = open(path_of_key_file, "wb")
                            keyfile.write(key)

                            # path of database

                            path_of_database_folder = "C:/TeXtCrYpTeR/database"

                            # if not

                            if not os.path.exists(path_of_database_folder):
                                os.mkdir(path_of_database_folder)

                                # path of database

                                path_of_database = "C:/TeXtCrYpTeR/database/database.csv"

                                # if not
                                if not os.path.isfile(path_of_database):

                                    # creating locker object for encryption

                                    keyfile = open(path_of_key_file, "rb")
                                    key_reader = keyfile.read()
                                    key_object = Fernet(key_reader)

                                    # email id

                                    email_id = email_id_entry.get()
                                    encoded_email_id = email_id.encode('utf-8')
                                    encrypted_email_id = key_object.encrypt(encoded_email_id)

                                    # user id

                                    user_id = create_user_id_entry.get()
                                    encoded_user_id = user_id.encode('utf-8')
                                    encrypted_user_id = key_object.encrypt(encoded_user_id)

                                    # password

                                    password = create_password_entry.get()
                                    encoeded_password = password.encode('utf-8')
                                    encrypted_password = key_object.encrypt(encoeded_password)

                                    # confirm password

                                    confirm_password = create_password_confirm_entry.get()
                                    encoded_confirm_password = confirm_password.encode('utf-8')
                                    encrypted_confirm_password = key_object.encrypt(encoded_confirm_password)

                                    # first name

                                    first_name = first_name_entry.get()
                                    encoded_first_name = first_name.encode('utf-8')
                                    encrypted_first_name = key_object.encrypt(encoded_first_name)

                                    # last name
                                    last_name = last_name_entry.get()
                                    encoded_last_name = last_name.encode('utf-8')
                                    encrypted_last_name = key_object.encrypt(encoded_last_name)

                                    database = open(path_of_database, "a", newline="")
                                    data_writer = csv.writer(database)
                                    data_writer.writerow([encrypted_email_id, encrypted_user_id, encrypted_password,encrypted_confirm_password, encrypted_first_name,encrypted_last_name])
                                    create_account_window.destroy()
                                    messagebox.showinfo(title="SUCCESS",message="ACCOUNT CREATED SUCCESSFULLY ON YOUR LOCAL DISK")
                                    main_window.deiconify()


                                else:
                                    messagebox.showerror(title="ERROR", message="DATA BREACHED")

                            else:
                                messagebox.showerror(title="ERROR", message="DATA BREACHED")

                        else:
                            messagebox.showerror(title="ERROR", message="DATA BREACHED")

                    else:
                        messagebox.showerror(title="ERROR", message="DATA BREACHED")

                else:

                    # path of key file
                    path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
                    keyfile = open(path_of_key_file, "rb")
                    key_reader = keyfile.read()
                    key_object = Fernet(key_reader)

                    path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                    # path of database
                    database = open(path_of_database,"r")
                    data_reader = csv.reader(database)

                    for eandu in data_reader:
                        # for email

                        e_id = eandu[0].strip('b')
                        e_id = e_id.replace("'","")
                        decrypted_e_id = key_object.decrypt(e_id)
                        decoded_e_id = decrypted_e_id.decode('utf-8')

                        # for user id

                        u_id = eandu[1].strip('b')
                        u_id = u_id.replace("'","")
                        decrypted_u_id = key_object.decrypt(u_id)
                        decoded_u_id = decrypted_u_id.decode('utf-8')

                        if email_id_entry.get() == decoded_e_id and create_user_id_entry.get() == decoded_u_id:
                            email_id_entry.delete(0,END)
                            create_user_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="BOTH EMAIL AND USER ID ALREADY EXIST TRY SOMETHING NEW")
                            break
                        
                        elif email_id_entry.get() == decoded_e_id:
                            email_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="EMAIL ID ALREADY EXIST TRY SOMETHING NEW")
                            break
                        
                        elif create_user_id_entry.get() == decoded_u_id:
                            create_user_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="EMAIL ID ALREADY EXIST TRY SOMETHING NEW")
                            break

                    else:
                        # email id

                        email_id = email_id_entry.get()
                        encoded_email_id = email_id.encode('utf-8')
                        encrypted_email_id = key_object.encrypt(encoded_email_id)

                        # user id

                        user_id = create_user_id_entry.get()
                        encoded_user_id = user_id.encode('utf-8')
                        encrypted_user_id = key_object.encrypt(encoded_user_id)

                        # password

                        password = create_password_entry.get()
                        encoeded_password = password.encode('utf-8')
                        encrypted_password = key_object.encrypt(encoeded_password)

                        # confirm password

                        confirm_password = create_password_confirm_entry.get()
                        encoded_confirm_password = confirm_password.encode('utf-8')
                        encrypted_confirm_password = key_object.encrypt(encoded_confirm_password)

                        # first name

                        first_name = first_name_entry.get()
                        encoded_first_name = first_name.encode('utf-8')
                        encrypted_first_name = key_object.encrypt(encoded_first_name)

                        # last name
                        last_name = last_name_entry.get()
                        encoded_last_name = last_name.encode('utf-8')
                        encrypted_last_name = key_object.encrypt(encoded_last_name)
                        
                        database = open(path_of_database, "a", newline="")
                        data_writer = csv.writer(database)
                        data_writer.writerow([encrypted_email_id,encrypted_user_id, encrypted_password,encrypted_confirm_password, encrypted_first_name,encrypted_last_name])
                        create_account_window.destroy()
                        messagebox.showinfo(title="SUCCESS",message="ACCOUNT CREATED SUCCESSFULLY ON YOUR LOCAL DISK")
                        main_window.deiconify()
                        
            if email_id_entry.get() == "":
                message_unsuccessful_email()
            elif create_user_id_entry.get() == "":
                message_unsuccessful_userid()
            elif create_password_entry.get() == "":
                message_unsuccessfull_password()
            elif len(create_password_entry.get()) <= 8:
                message_password_length_error()
            elif create_password_confirm_entry.get() == "":
                message_unsuccessful_confirm_password()
            elif create_password_entry.get() != create_password_confirm_entry.get():
                message_unsuccessful_password_missmatch()
            elif first_name_entry.get() == "":
                message_unsuccessful_firtname_empty()
            elif last_name_entry.get() == "":
                message_unsuccesful_lastname_empty()
            else:
                successfull()

        def register_now_button(event):
            # if emial is empty

            def message_unsuccessful_email():
                messagebox.showerror(title="ERROR", message="EMAIL CANNOT BE EMPTY")

            # if user id is blank

            def message_unsuccessful_userid():
                messagebox.showerror(title="ERROR", message="USER ID CANNOT BE EMPTY")

            # if password entry is blank

            def message_unsuccessfull_password():
                messagebox.showerror(title="ERROR", message="PASSWORD CANNOT BE EMPTY")

            # if lenth is les than 8 character
            def message_password_length_error():
                messagebox.showerror(title="ERROR", message="PASSWORD CANNOT BE MORE LESS THAN 8 CHARACTERS")

            # if confirm psasword is empty

            def message_unsuccessful_confirm_password():
                messagebox.showerror(title="ERROR", message="PLEASE CONFIRM THE PASSWORD TO CONTINUE")

            # if password doesnot match the

            def message_unsuccessful_password_missmatch():
                messagebox.showerror(title="ERROR", message="PASSWORD DID NOT MATCHED")

            # if first name is empty

            def message_unsuccessful_firtname_empty():
                messagebox.showerror(title="ERROR", message="FIRST NAME CANNOT BE EMPTY")

            # if last name is empty

            def message_unsuccesful_lastname_empty():
                messagebox.showerror(title="ERROR", message="LAST NAME CANNOT BE EMPTY")

            # when evrything is alright

            def successfull():
                # path of Textcrypter
                path_of_textcrypter = "C:/TeXtCrYpTeR"

                # if not
                if not os.path.exists(path_of_textcrypter):
                    os.mkdir(path_of_textcrypter)

                    # path of key folder
                    path_of_key_folder = "C:/TeXtCrYpTeR/key"

                    # if not

                    if not os.path.exists(path_of_key_folder):
                        os.mkdir(path_of_key_folder)

                        # path of key file
                        path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"

                        # if not

                        if not os.path.isfile(path_of_key_file):

                            # generate key file

                            key = Fernet.generate_key()
                            keyfile = open(path_of_key_file, "wb")
                            keyfile.write(key)

                            # path of database

                            path_of_database_folder = "C:/TeXtCrYpTeR/database"

                            # if not

                            if not os.path.exists(path_of_database_folder):
                                os.mkdir(path_of_database_folder)

                                # path of database

                                path_of_database = "C:/TeXtCrYpTeR/database/database.csv"

                                # if not
                                if not os.path.isfile(path_of_database):

                                    # creating locker object for encryption

                                    keyfile = open(path_of_key_file, "rb")
                                    key_reader = keyfile.read()
                                    key_object = Fernet(key_reader)

                                    # email id

                                    email_id = email_id_entry.get()
                                    encoded_email_id = email_id.encode('utf-8')
                                    encrypted_email_id = key_object.encrypt(encoded_email_id)

                                    # user id

                                    user_id = create_user_id_entry.get()
                                    encoded_user_id = user_id.encode('utf-8')
                                    encrypted_user_id = key_object.encrypt(encoded_user_id)

                                    # password

                                    password = create_password_entry.get()
                                    encoeded_password = password.encode('utf-8')
                                    encrypted_password = key_object.encrypt(encoeded_password)

                                    # confirm password

                                    confirm_password = create_password_confirm_entry.get()
                                    encoded_confirm_password = confirm_password.encode('utf-8')
                                    encrypted_confirm_password = key_object.encrypt(encoded_confirm_password)

                                    # first name

                                    first_name = first_name_entry.get()
                                    encoded_first_name = first_name.encode('utf-8')
                                    encrypted_first_name = key_object.encrypt(encoded_first_name)

                                    # last name
                                    last_name = last_name_entry.get()
                                    encoded_last_name = last_name.encode('utf-8')
                                    encrypted_last_name = key_object.encrypt(encoded_last_name)

                                    database = open(path_of_database, "a", newline="")
                                    data_writer = csv.writer(database)
                                    data_writer.writerow([encrypted_email_id, encrypted_user_id, encrypted_password,encrypted_confirm_password, encrypted_first_name,encrypted_last_name])
                                    create_account_window.destroy()
                                    messagebox.showinfo(title="SUCCESS",message="ACCOUNT CREATED SUCCESSFULLY ON YOUR LOCAL DISK")
                                    main_window.deiconify()


                                else:
                                    messagebox.showerror(title="ERROR", message="DATA BREACHED")

                            else:
                                messagebox.showerror(title="ERROR", message="DATA BREACHED")

                        else:
                            messagebox.showerror(title="ERROR", message="DATA BREACHED")

                    else:
                        messagebox.showerror(title="ERROR", message="DATA BREACHED")

                else:

                    # path of key file
                    path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
                    keyfile = open(path_of_key_file, "rb")
                    key_reader = keyfile.read()
                    key_object = Fernet(key_reader)

                    path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                    # path of database
                    database = open(path_of_database,"r")
                    data_reader = csv.reader(database)

                    for eandu in data_reader:
                        # for email

                        e_id = eandu[0].strip('b')
                        e_id = e_id.replace("'","")
                        decrypted_e_id = key_object.decrypt(e_id)
                        decoded_e_id = decrypted_e_id.decode('utf-8')

                        # for user id

                        u_id = eandu[1].strip('b')
                        u_id = u_id.replace("'","")
                        decrypted_u_id = key_object.decrypt(u_id)
                        decoded_u_id = decrypted_u_id.decode('utf-8')

                        if email_id_entry.get() == decoded_e_id and create_user_id_entry.get() == decoded_u_id:
                            email_id_entry.delete(0,END)
                            create_user_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="BOTH EMAIL AND USER ID ALREADY EXIST TRY SOMETHING NEW")
                            break
                        
                        elif email_id_entry.get() == decoded_e_id:
                            email_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="EMAIL ID ALREADY EXIST TRY SOMETHING NEW")
                            break
                        
                        elif create_user_id_entry.get() == decoded_u_id:
                            create_user_id_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="EMAIL ID ALREADY EXIST TRY SOMETHING NEW")
                            break

                    else:
                        # email id

                        email_id = email_id_entry.get()
                        encoded_email_id = email_id.encode('utf-8')
                        encrypted_email_id = key_object.encrypt(encoded_email_id)

                        # user id

                        user_id = create_user_id_entry.get()
                        encoded_user_id = user_id.encode('utf-8')
                        encrypted_user_id = key_object.encrypt(encoded_user_id)

                        # password

                        password = create_password_entry.get()
                        encoeded_password = password.encode('utf-8')
                        encrypted_password = key_object.encrypt(encoeded_password)

                        # confirm password

                        confirm_password = create_password_confirm_entry.get()
                        encoded_confirm_password = confirm_password.encode('utf-8')
                        encrypted_confirm_password = key_object.encrypt(encoded_confirm_password)

                        # first name

                        first_name = first_name_entry.get()
                        encoded_first_name = first_name.encode('utf-8')
                        encrypted_first_name = key_object.encrypt(encoded_first_name)

                        # last name
                        last_name = last_name_entry.get()
                        encoded_last_name = last_name.encode('utf-8')
                        encrypted_last_name = key_object.encrypt(encoded_last_name)
                        
                        database = open(path_of_database, "a", newline="")
                        data_writer = csv.writer(database)
                        data_writer.writerow([encrypted_email_id, encrypted_user_id, encrypted_password,encrypted_confirm_password, encrypted_first_name,encrypted_last_name])
                        create_account_window.destroy()
                        messagebox.showinfo(title="SUCCESS",message="ACCOUNT CREATED SUCCESSFULLY ON YOUR LOCAL DISK")
                        main_window.deiconify()
                

            if email_id_entry.get() == "":
                message_unsuccessful_email()
            elif create_user_id_entry.get() == "":
                message_unsuccessful_userid()
            elif create_password_entry.get() == "":
                message_unsuccessfull_password()
            elif len(create_password_entry.get()) <= 8:
                message_password_length_error()
            elif create_password_confirm_entry.get() == "":
                message_unsuccessful_confirm_password()
            elif create_password_entry.get() != create_password_confirm_entry.get():
                message_unsuccessful_password_missmatch()
            elif first_name_entry.get() == "":
                message_unsuccessful_firtname_empty()
            elif last_name_entry.get() == "":
                message_unsuccesful_lastname_empty()
            else:
                successfull()


        # final sign up button

        create_button_pic = PhotoImage(file="assets/create.png")
        create_button_holder = tk.Button(create_account_window, image=create_button_pic, command=register_now)
        create_button_holder.config(activebackground="#222222", relief=FLAT, borderwidth=0, bg="#222222",cursor="hand2")
        create_button_holder.place(x=240, y=433)
        create_account_window.bind('<Return>', register_now_button)

        # def final close question

        def confirm_close_create_ccount_window():
            ask = messagebox.askyesno(title="EXIT TeXtCrYpTeR", message="DO YOU WANT TO EXIT")
            if ask:
                create_account_window.destroy()
                main_window.destroy()

        create_account_window.protocol("WM_DELETE_WINDOW", confirm_close_create_ccount_window)
        create_account_window.mainloop()

    # create account window open button

    create_account_img = PhotoImage(file="assets/create_account.png")
    create_account = tk.Button(main_window, image=create_account_img, command=create_account_first, relief="flat",borderwidth=0)
    create_account.config(bg="#222222", activebackground="#222222",cursor="hand2")
    create_account.place(x=406, y=93)

    # forgot password

    def pass_show(event):
        main_window.withdraw()
        
        password_change_window = tk.Toplevel()
        password_change_window.title("TeXtCrYpTeR (CHANGE PASSWORD)")
        password_change_window.grab_set()
        
        password_change_window.maxsize(width=500,height=400)
        password_change_window.minsize(width=500,height=400)
        
        password_change_window.resizable(0,0)
        
        screen_width = password_change_window.winfo_screenwidth()
        screen_height = password_change_window.winfo_screenheight()
        
        app_width = 500
        app_height = 400
        
        a = (screen_width/2) - (app_width/2)
        b = (screen_height/2) - (app_height/2)
        
        password_change_window.geometry(f"{app_width}x{app_height}+{int(a)}+{int(b)}")
        
        logo = tk.PhotoImage(file="assets/textcrypter.png")
        logo_place = tk.Label(password_change_window, image=logo, bg="#222222")
        logo_place.place(x=140, y=20)
        
        container_img = Image.open("assets/forgot.png")
        container_image = ImageTk.PhotoImage(container_img)
        container_image_place = tk.Label(password_change_window, image=container_image)
        container_image_place.place(x=30, y=100)
        
        # version

        version = tk.Label(password_change_window, text="Version 1.0", font=("monospace", 8, "bold"))
        version.config(bg="#222222", fg="#DF1FE3")
        version.place(x=366, y=66)
        
        def back_button():
            password_change_window.destroy()
            main_window.deiconify()

        img_back = Image.open("assets/back.png")
        image_back = ImageTk.PhotoImage(img_back)
        image_back_place = tk.Button(password_change_window, image=image_back, command=back_button)
        image_back_place.config(bg="#222222", activebackground="#222222", relief=FLAT,cursor="hand2")
        image_back_place.place(x=35, y=40)
        
        
        # pre user id
        
        pre_user_id_variable = StringVar()

        pre_user_id_entry = tk.Entry(password_change_window, textvariable=pre_user_id_variable,font=("monospace", 13, "bold"))
        pre_user_id_entry.config(bg="white", relief=FLAT, width=23, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray")
        pre_user_id_entry.place(x=227, y=124)
        
        current_password_variable = StringVar()
        
        current_password_entry = tk.Entry(password_change_window, textvariable=current_password_variable,font=("monospace",13,"bold"))
        current_password_entry.config(bg="white", relief=FLAT, width=23, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray",show="*")
        current_password_entry.place(x=227,y=176)
        
        new_password__variable = StringVar()
        
        new_password_entry = tk.Entry(password_change_window, textvariable=new_password__variable,font=("monospace",13,"bold"))
        new_password_entry.config(bg="white", relief=FLAT, width=23, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray",show="*")
        new_password_entry.place(x=227,y=229)
        
        new_confirm_password_variable = StringVar()
        
        new_confirm_password_entry = tk.Entry(password_change_window, textvariable=new_confirm_password_variable,font=("monospace",13,"bold"))
        new_confirm_password_entry.config(bg="white", relief=FLAT, width=23, highlightbackground="white",highlightcolor="white", highlightthickness=1, fg="gray17",
        insertbackground="gray",show="*")
        new_confirm_password_entry.place(x=227,y=283)
        

        def change_now():
            def unsuccessful_blank_user_id():
                messagebox.showerror(title="ERROR",message="USER ID CANNOT BE EMPTY")
            
            def unsuccessful_blank_current_password_empty():
                messagebox.showerror(title="ERROR",message="PASSWORD CANNOT BE EMPTY")
            
            def unsuccessful_blank_new_password_empty():
                messagebox.showerror(title="ERROR",message="NEW PASSWORD CANNOT BE EMPTY")
                
            def unsucessful_blank_confirm_password_empty():
                messagebox.showerror(title="ERROR",message="CONFIRM PASSWORD CANNOT BE EMPTY")
                
            def password_match_error():
                messagebox.showerror(title="ERROR",message="PASSWORD DID NOT MATCHED")
            
            def successful():
                # path of key file
            
                path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
                keyfile = open(path_of_key_file, "rb")
                key_reader = keyfile.read()
                key_object = Fernet(key_reader)
            
                # path of database 
                path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                database = open(path_of_database,"r")
                data_reader = csv.reader(database)
            
                for uandp in data_reader:
                    u_id = uandp[1].strip('b')
                    u_id = u_id.replace("'","")
                    decrypted_u_id = key_object.decrypt(u_id)
                    decoded_u_id = decrypted_u_id.decode('utf-8')
                    
                    pwd = uandp[2].strip('b')
                    pwd = pwd.replace("'","")
                    decrypted_password = key_object.decrypt(pwd)
                    decoded_password = decrypted_password.decode('utf-8')
                    
                    if decoded_u_id == pre_user_id_entry.get() and decoded_password == current_password_entry.get():
                        new_password = new_confirm_password_entry.get()
                        encoded_new_password = new_password.encode('utf-8')
                        encrypted_new_password = key_object.encrypt(encoded_new_password)
                        
                        new_confirm_password = new_confirm_password_entry.get()
                        encoded_new_confirm_password = new_confirm_password.encode('utf-8')
                        encrypted_new_confirm_password = key_object.encrypt(encoded_new_confirm_password)

                        # path of database 
                        path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                        database = open(path_of_database,"r")
                        data_reader = csv.reader(database)        
                        for row in data_reader:
                            database = open(path_of_database,"r")
                            database = ''.join([i for i in database])
                            database = database.replace(row[2],str(encrypted_new_password))
                            database = database.replace(row[3],str(encrypted_new_confirm_password))
                            replaced = open(path_of_database,"w ")
                            replaced.writelines(database)
                            password_change_window.destroy()
                            messagebox.showinfo(title="SUCCESS",message="PASSWORD UPDATED SUCCESSFULY")
                            main_window.deiconify()
                            break
   
                        break
                    
                    elif pre_user_id_entry.get() == decoded_u_id and current_password_entry.get() != decoded_password:
                        current_password_entry.delete(0,END)
                        messagebox.showerror(title="ERROR",message="PASSWORD MISSMATCHED FOR USER ID"+pre_user_id_entry.get())
                        break
                    
                else:
                    messagebox.showerror(title="ERROR",message="NO USER NAME FOUND"+" "+pre_user_id_entry.get())
                    pre_user_id_entry.delete(0,END)
                    current_password_entry.delete(0,END)
                    
        
                
            if pre_user_id_entry.get() == "":
                unsuccessful_blank_user_id()
            
            elif current_password_entry.get() == "":
                unsuccessful_blank_current_password_empty()
            
            elif new_password_entry.get() == "":
                unsuccessful_blank_new_password_empty()
                
            elif new_confirm_password_entry.get() == "":
                unsucessful_blank_confirm_password_empty()
                
            elif new_password_entry.get() != new_confirm_password_entry.get():
                password_match_error()
            
            else:
                successful()
            

            
        def change_now_button(event):
            
            def unsuccessful_blank_user_id():
                messagebox.showerror(title="ERROR",message="USER ID CANNOT BE EMPTY")
            
            def unsuccessful_blank_current_password_empty():
                messagebox.showerror(title="ERROR",message="PASSWORD CANNOT BE EMPTY")
            
            def unsuccessful_blank_new_password_empty():
                messagebox.showerror(title="ERROR",message="NEW PASSWORD CANNOT BE EMPTY")
                
            def unsucessful_blank_confirm_password_empty():
                messagebox.showerror(title="ERROR",message="CONFIRM PASSWORD CANNOT BE EMPTY")
            
            def password_match_error():
                messagebox.showerror(title="ERROR",message="PASSWORD DID NOT MATCHED")
            
            def successful():
                # path of key file
            
                path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
                keyfile = open(path_of_key_file, "rb")
                key_reader = keyfile.read()
                key_object = Fernet(key_reader)
            
                # path of database 
                path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                database = open(path_of_database,"r")
                data_reader = csv.reader(database)
            
                for uandp in data_reader:
                    u_id = uandp[1].strip('b')
                    u_id = u_id.replace("'","")
                    decrypted_u_id = key_object.decrypt(u_id)
                    decoded_u_id = decrypted_u_id.decode('utf-8')
                    
                    pwd = uandp[2].strip('b')
                    pwd = pwd.replace("'","")
                    decrypted_password = key_object.decrypt(pwd)
                    decoded_password = decrypted_password.decode('utf-8')
                    
                    if decoded_u_id == pre_user_id_entry.get() and decoded_password == current_password_entry.get():
                        new_password = new_confirm_password_entry.get()
                        encoded_new_password = new_password.encode('utf-8')
                        encrypted_new_password = key_object.encrypt(encoded_new_password)

                        
                        # path of database 
                        path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                        database = open(path_of_database,"r")
                        data_reader = csv.reader(database)        
                        for row in data_reader:
                            database = open(path_of_database,"r")
                            database = ''.join([i for i in database])
                            database = database.replace(row[2],str(encrypted_new_password))
                            replaced = open(path_of_database,"w")
                            replaced.writelines(database)
                            replaced.close()
                            password_change_window.destroy()
                            messagebox.showinfo(title="SUCCESS",message="PASSWORD UPDATED SUCCESSFULY")
                            main_window.deiconify()
                            break

                        break
                    
                    elif pre_user_id_entry.get() == decoded_u_id and current_password_entry.get() != decoded_password:
                        current_password_entry.delete(0,END)
                        messagebox.showerror(title="ERROR",message="PASSWORD MISSMATCHED FOR USER ID"+pre_user_id_entry.get())
                        break
                    
                else:
                    messagebox.showerror(title="ERROR",message="NO USER NAME FOUND"+" "+pre_user_id_entry.get())
                    pre_user_id_entry.delete(0,END)
                    current_password_entry.delete(0,END)
            
            
            
            if pre_user_id_entry.get() == "":
                unsuccessful_blank_user_id()
            
            elif current_password_entry.get() == "":
                unsuccessful_blank_current_password_empty()
            
            elif new_password_entry.get() == "":
                unsuccessful_blank_new_password_empty()
                
            elif new_confirm_password_entry.get() == "":
                unsucessful_blank_confirm_password_empty()
                
            elif new_password_entry.get() != new_confirm_password_entry.get():
                password_match_error()
            
            else:
                successful()
            
            
    
        change_password= PhotoImage(file="assets/change_password.png")
        change_password_button_holder = tk.Button(password_change_window, image=change_password, command=change_now)
        change_password_button_holder.config(activebackground="#222222", relief=FLAT, borderwidth=0, bg="#222222",cursor="hand2")
        change_password_button_holder.place(x=160, y=350)
        password_change_window.bind('<Return>', change_now_button)
    
        def confirm_close_password_window():
            
            ask = messagebox.askyesno(title="EXIT",message="DO YOU WANT TO EXIT")
            
            if ask:
                password_change_window.destroy()
                main_window.destroy()
        
        password_change_window.protocol("WM_DELETE_WINDOW",confirm_close_password_window)
        password_change_window.mainloop()

    forgot_password_img = PhotoImage(file="assets/Forgot_password.png")
    forgot_password = tk.Label(main_window, image=forgot_password_img)
    forgot_password.config(bg="#579be9",cursor="hand2")
    forgot_password.place(x=320, y=246)
    forgot_password.bind('<Button-1>', pass_show)

    # access button

    def access_now():
        
        def unsuccessful_user_id_empty():
            messagebox.showerror(title="ERROR", message="NO USER ID IS GIVEN")

        def unsuccessful_password_empty():
            messagebox.showerror(title="ERROR", message="NO PASSWORD GIVEN FOR USER ID " + user_id_entry.get())

        def successful():
            
            def cheking_done():
            
                path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
            
                if not os.path.isfile(path_of_key_file):
                    user_id_entry.delete(0,END)
                    password_entry.delete(0,END)
                    messagebox.showerror(title="ERROR",message="NO USER ID FOUND"+user_id_entry.get())
                
                    ask = messagebox.askyesno(title="CREATE ACCOUNT",message="DO YOU WANT TO CREATE ACCOUNT")
                
                    if ask:
                        create_account_first()
            
                else:
                
                    keyfile = open(path_of_key_file,"rb")
                    key_reader = keyfile.read()
                    key_object = Fernet(key_reader)
                
                    # path of database 
                
                    path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                
                    database = open(path_of_database,"r")
                    data_reader = csv.reader(database)
                
                    for uandp in data_reader:
                        u_id = uandp[1].strip('b')
                        u_id = u_id.replace("'","")
                        decrypted_u_id = key_object.decrypt(u_id)
                        decoded_u_id = decrypted_u_id.decode('utf-8')
                    
                        pwd = uandp[2].strip('b')
                        pwd = pwd.replace("'","")
                        decrypted_password = key_object.decrypt(pwd)
                        decoded_password = decrypted_password.decode('utf-8')
                    
                        if decoded_u_id == user_id_entry.get() and decoded_password == password_entry.get():
                           
                            unpicpad = tk.PhotoImage(file="assets/padlock_unlock.png")
                            unpicpad_placer = tk.Label(main_window,image=unpicpad, bg="#222222")
                            unpicpad_placer.place(x=0, y=120)
                            
                            lock.destroy()
                            unlock = tk.Label(main_window, text="●", font=("monospace", 15, "bold"))
                            unlock.config(fg="#33cc00", height=1, width=1)
                            unlock.place(x=68, y=190)
                            
                            locked_frame.destroy()
                            
                            unlocked_frame = tk.Frame(main_window, width=116, bg="white", height=40)
                            unlocked_frame.place(x=19, y=265)
                            # status
                            unlocked_place = tk.Label(unlocked_frame, text="STATUS :  UNLOCKED", font=("Arial", 8, 'bold'))
                            unlocked_place.config(bg="#222222", fg="#33cc00", relief=FLAT)
                            unlocked_place.place(x=1, y=2)
                            
                            user_id_entry.delete(0,END)
                            password_entry.delete(0,END)
                            messagebox.showinfo(title="SUCCESS",message="SUCCESSFULY LOGED IN")
                            
                            
                            ####################################################################### main work tart here #############################################################
                            
                            main_window.withdraw()
                            
                            # main working window
                            
                            working_window = tk.Toplevel()
                            working_window.grab_set()
                            
                            working_window.title("TeXtCrYpTeR")
                            
                            working_window.resizable(0,0)
                            
                            working_window.maxsize(width=700,height=500)
                            working_window.minsize(width=700,height=500)
                            
                            screen_width = working_window.winfo_screenwidth()
                            screen_height = working_window.winfo_screenheight()
                            
                            app_width = 700
                            app_height = 500
                            
                            x = (screen_width/2) - (screen_height/2)
                            y = (app_width/2) - (app_height/2)
                            
                            working_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            def log_out():
                                ask = messagebox.askyesno(title="EXIT",message="DO YOU WANT TO EXIT")
                                
                                if ask:
                                    working_window.destroy()
                                    main_window.deiconify()
                            
                            
                                    
                                    
                            def confirm_close_working_window():
                                messagebox.showerror(title="ERROR",message="YOU CANNOT EXIT WITHOUT LOGGING OUT")
                             
                        
                            working_window.protocol("WM_DELETE_WINDOW",confirm_close_working_window)
                            working_window.mainloop()
                            break
                        
                        
                        elif user_id_entry.get() == decoded_u_id and password_entry.get() != decoded_password:
                            password_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="PASSWORD MISSMATCHED FOR USER ID"+user_id_entry.get())
                            break
                   
                    else:
                        messagebox.showerror(title="ERROR",message="NO USER NAME FOUND"+" "+user_id_entry.get())
                        user_id_entry.delete(0,END)
                        password_entry.delete(0,END)
                           
            
            cheking_done()
                
                
        if user_id_entry.get() == "":
            unsuccessful_user_id_empty()
        elif password_entry.get() == "":
            unsuccessful_password_empty()
        else:
            successful()

    def access_now_button(event):
        def unsuccessful_user_id_empty():
            messagebox.showerror(title="ERROR", message="NO USER ID IS GIVEN")

        def unsuccessful_password_empty():
            messagebox.showerror(title="ERROR", message="NO PASSWORD GIVEN FOR USER ID " + user_id_entry.get())

        def successful():
            def cheking_done():
            
                path_of_key_file = "C:/TeXtCrYpTeR/key/keyfile.key"
            
                if not os.path.isfile(path_of_key_file):
                    user_id_entry.delete(0,END)
                    password_entry.delete(0,END)
                    messagebox.showerror(title="ERROR",message="NO USER ID FOUND"+user_id_entry.get())
                
                    ask = messagebox.askyesno(title="CREATE ACCOUNT",message="DO YOU WANT TO CREATE ACCOUNT")
                
                    if ask:
                        create_account_first()
            
                else:
                
                    keyfile = open(path_of_key_file,"rb")
                    key_reader = keyfile.read()
                    key_object = Fernet(key_reader)
                
                    # path of database 
                
                    path_of_database = "C:/TeXtCrYpTeR/database/database.csv"
                
                    database = open(path_of_database,"r")
                    data_reader = csv.reader(database)
                
                    for uandp in data_reader:
                        u_id = uandp[1].strip('b')
                        u_id = u_id.replace("'","")
                        decrypted_u_id = key_object.decrypt(u_id)
                        decoded_u_id = decrypted_u_id.decode('utf-8')
                    
                        pwd = uandp[2].strip('b')
                        pwd = pwd.replace("'","")
                        decrypted_password = key_object.decrypt(pwd)
                        decoded_password = decrypted_password.decode('utf-8')
                    
                        if decoded_u_id == user_id_entry.get() and decoded_password == password_entry.get():
                            
                            picpad_placer.destroy()
                           
                            unpicpad = tk.PhotoImage(file="assets/padlock_unlock.png")
                            unpicpad_placer = tk.Label(main_window,image=unpicpad, bg="#222222")
                            unpicpad_placer.place(x=0, y=120)
                            
                            lock.destroy()
                            unlock = tk.Label(main_window, text="●", font=("monospace", 15, "bold"))
                            unlock.config(fg="#33cc00", height=1, width=1)
                            unlock.place(x=68, y=190)
                            
                            locked_frame.destroy()
                            
                            unlocked_frame = tk.Frame(main_window, width=116, bg="white", height=40)
                            unlocked_frame.place(x=19, y=265)
                            # status
                            unlocked_place = tk.Label(unlocked_frame, text="STATUS :  UNLOCKED", font=("Arial", 8, 'bold'))
                            unlocked_place.config(bg="#222222", fg="#33cc00", relief=FLAT)
                            unlocked_place.place(x=1, y=2)
                            
                            user_id_entry.delete(0,END)
                            password_entry.delete(0,END)
                            messagebox.showinfo(title="SUCCESS",message="SUCCESSFULY LOGED IN")
                            ####################################################################### main work tart here #############################################################
                            
                            main_window.withdraw()
                            
                            # main working window
                            
                            working_window = tk.Toplevel()
                            working_window.grab_set()
                            
                            working_window.title("TeXtCrYpTeR")
                            
                            working_window.resizable(0,0)
                            
                            working_window.maxsize(width=750,height=480)
                            working_window.minsize(width=750,height=480)
                            
                            screen_width = working_window.winfo_screenwidth()
                            screen_height = working_window.winfo_screenheight()
                            
                            app_width = 700
                            app_height = 500
                            
                            x = (screen_width/2) - (app_width/2)
                            y = (screen_height/2) - (app_height/2)
                            
                            working_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            def log_out():
                                ask = messagebox.askyesno(title="EXIT",message="DO YOU WANT TO EXIT")
                                
                                if ask:
                                    working_window.destroy()
                                    main_window.deiconify()
                                    
                                    
                            def confirm_close_working_window():
                                messagebox.showerror(title="ERROR",message="YOU CANNOT EXIT WITHOUT LOGGING OUT")
                             
                        
                            working_window.protocol("WM_DELETE_WINDOW",confirm_close_working_window)
                            working_window.mainloop()
                            break
                            
                        
                        elif user_id_entry.get() == decoded_u_id and password_entry.get() != decoded_password:
                            password_entry.delete(0,END)
                            messagebox.showerror(title="ERROR",message="PASSWORD MISSMATCHED FOR USER ID"+user_id_entry.get())
                            break
                   
                    else:
                        messagebox.showerror(title="ERROR",message="NO USER NAME FOUND"+" "+user_id_entry.get())
                        user_id_entry.delete(0,END)
                        password_entry.delete(0,END)
                           
            
            cheking_done()
            
        if user_id_entry.get() == "":
            unsuccessful_user_id_empty()
        elif password_entry.get() == "":
            unsuccessful_password_empty()
        else:
            successful()

    access_button_pic = PhotoImage(file="assets/access.png")
    access_button_holder = tk.Button(main_window, image=access_button_pic, command=access_now)
    access_button_holder.config(activebackground="#222222", relief=FLAT, borderwidth=0, bg="#222222",cursor="hand2")
    access_button_holder.place(x=240, y=295)
    main_window.bind('<Return>', access_now_button)

    # main window close confirm
 
    def confirm_close():
        message = messagebox.askyesno(title="EXIT TeXtCrYpTeR", message="DO YOU WANT TO EXIT")
        if message:
            main_window.destroy()

    main_window.protocol("WM_DELETE_WINDOW", confirm_close)
    main_window.mainloop()


at_first()

