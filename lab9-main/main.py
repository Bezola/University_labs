import os
import json
import tkinter as tk
import re
from tkinter.messagebox import showwarning, showinfo

font = 'Georgia 15'
show_password_setting = '*'

root = tk.Tk()
root.title("Вход в учётную запись")
root.geometry("600x350")
root.resizable(False, False)

if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump([], f)
        pass


# -----------------------------------------------------
def password_ableness(symbol):
    return re.fullmatch(r"[a-zA-Z\d!@#$%^&*()_+]*", symbol) is not None


def show_password():
    global show_password_setting
    if show_password_setting == '*':
        show_password_setting = ''
        show_pswrd_btn.config(text='Скрыть пароль')
        try:
            reg_show_pswrd_btn.config(text='Скрыть пароль')
        except NameError:
            pass
        except tk.TclError:
            pass

    else:
        show_password_setting = '*'
        show_pswrd_btn.config(text='Показать пароль')
        try:
            reg_show_pswrd_btn.config(text='Показать пароль')
        except NameError:
            pass
        except tk.TclError:
            pass

    password_box.config(show=show_password_setting)
    try:
        reg_password_box.config(show=show_password_setting)
    except NameError:
        pass
    except tk.TclError:
        pass


def reg_window():
    global window
    window = tk.Tk()
    window.title("Регистрация")
    window.geometry("600x280")
    window.resizable(False, False)

    label = tk.Label(window, text="Имя пользователя", font=font)
    label.pack()

    global reg_login_box
    reg_login_box = tk.Entry(window, font=font)
    reg_login_box.place(x=155, y=45)

    label = tk.Label(window, text="Придумайте пароль", font=font)
    label.place(x=190, y=90)

    global reg_password_box
    reg_password_box = tk.Entry(window, font=font, validate='key', validatecommand=check, show=show_password_setting)
    reg_password_box.place(x=155, y=140)

    global reg_show_pswrd_btn
    reg_show_pswrd_btn = tk.Button(window, text="Показать пароль", font='Georgia 9', command=show_password)
    reg_show_pswrd_btn.place(x=450, y=140)

    login_btn = tk.Button(window, text="Регистрация", font=font, command=register)
    login_btn.place(x=215, y=200)


def register():
    login_name = reg_login_box.get()
    password_name = reg_password_box.get()
    if len(login_name) < 4:
        showwarning('Внимание', 'Имя не может быть короче 4 знаков')
    else:
        if len(password_name) < 4:
            showwarning('Внимание', 'Пароль не может быть короче 4 знаков')
        else:
            with open("users.json", "r") as read_file:
                try:
                    users_data = list(json.load(read_file))
                except json.JSONDecodeError:
                    users_data = None

            with open("users.json", "w") as f:  # Проверка на наличие пользователя в базе
                user_is_exists = False
                if users_data is not None:
                    for user in users_data:
                        if user['login'] == login_name:
                            user_is_exists = True
                            showwarning('Ошибка', 'Такое имя пользователя уже используется.')
                            json.dump(users_data, f)

                else:
                    users_data = []
                if not user_is_exists:
                    users_data.append({'login': login_name, "password": password_name})
                    # print('пользователь', login_name, 'зарегестрирован')
                    showinfo('Запись создана', 'Вы успешно зарегестрированы!')
                    json.dump(users_data, f)
                    window.destroy()


def login():
    login_name = login_box.get()
    password_name = password_box.get()
    with open("users.json", "r") as read_file:
        try:
            users_data = list(json.load(read_file))
        except json.JSONDecodeError:
            users_data = None

    with open("users.json", "w") as file:  # Проверка на наличие пользователя в базе
        user_is_exists = False
        if users_data is not None:
            for user in users_data:
                if user['login'] == login_name and user['password'] == password_name:
                    user_is_exists = True
                    showinfo('Вход прошел успешно', 'Вход совершен')
                    program_start(login_name)

        if not user_is_exists:
            if users_data is None:
                users_data = []
            showwarning('Ошибка', 'Неверное имя пользователя или пароль')
        json.dump(users_data, file)


def program_start(login):
    root.title("Добро пожаловать " + login)
    root.geometry("1000x650")
    root.resizable(False, False)
    label.destroy(), login_box.destroy(), label2.destroy(), password_box.destroy(), show_pswrd_btn.destroy()
    login_btn.destroy(), register_btn.destroy()

    label3 = tk.Label(text="Добро пожаловать, " + login + '!', font=font)
    label3.pack()


check = (root.register(password_ableness), "%P")
#  ----------------------------------------------------

label = tk.Label(text="Имя пользователя", font=font)
label.pack()

login_box = tk.Entry(font=font)
login_box.place(x=155, y=45)

label2 = tk.Label(text="Пароль", font=font)
label2.place(x=250, y=90)

password_box = tk.Entry(font=font, validate='key', validatecommand=check, show=show_password_setting)
password_box.place(x=155, y=140)

show_pswrd_btn = tk.Button(text="Показать пароль", font='Georgia 9', command=show_password)
show_pswrd_btn.place(x=450, y=140)

login_btn = tk.Button(text="Войти", font=font, command=login)
login_btn.place(x=250, y=200)

register_btn = tk.Button(text="Создать аккаунт", font=font, command=reg_window)
register_btn.place(x=195, y=270)

root.mainloop()
