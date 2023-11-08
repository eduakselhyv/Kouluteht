import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Tietokanta")
root.geometry("800x400")

username_var=StringVar()
password_var=StringVar()
task_var=StringVar()
edited_task=StringVar()

logged_in_as = ""

username = username_var.get()
password = password_var.get()
task = task_var.get()

conn = sqlite3.connect("login.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
          username TEXT PRIMARY KEY,
          password TEXT
)''')

conn = sqlite3.connect("tasklist.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        logged_in_as TEXT,
        task TEXT
)''')

def login_submit():
    global logged_in_as
    try:
        username = username_var.get()
        password = password_var.get()
        user = try_login(username, password)

        if user:
            response = messagebox.showinfo("Alert", "Kirjauduttu Sisään!")
            logged_in_as = username
            logged_in()
            display_tasks()
        else:
            response = messagebox.showinfo("Alert", "Virheellinen Käyttäjänimi/Salasana!")
    except:
        response = messagebox.showinfo("Alert", "Virheellinen Käyttäjänimi/Salasana!")

def register_submit():
    username = username_var.get()
    password = password_var.get()

    if username_exists(username):
        response = messagebox.showinfo("Alert", "Käyttäjänimi on jo käytössä!")

    elif (' ' in username) == True or (' ' in password) == True:
        response = messagebox.showinfo("Alert", "Käyttäjänimi ja salasana ei saa sisältää välilyöntejä!")

    elif len(username) == 0 or len(password) == 0:
        response = messagebox.showinfo("Alert", "Anna Käyttäjänimi ja salasana!")

    else:
        login_create(username, password)
        response = messagebox.showinfo("Alert", "Käyttäjä luotu!")

def username_exists(username):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()

    conn.close()

    return user is not None

def login_create(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
              username TEXT PRIMARY KEY,
              password TEXT
    )''')
    
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    conn.commit()
    conn.close()

def try_login(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()

    conn.close()
    return user

def logged_in():
    global username_box, password_box, login_btn, logout_btn, register_btn, logged_user, space, new_task_box, edit_task_btn, delete_task_btn, new_task_btn, task_var, edited_task

    username_box.destroy()
    password_box.destroy()

    login_btn.destroy()
    register_btn.destroy()

    logged_user = Label(root, text="Logged in as: " + logged_in_as)
    logged_user.grid(row=0, column=0, columnspan=1)
    
    logout_btn = Button(root, text="Logout", command=logout)
    logout_btn.grid(row=1, column=0, columnspan=1)

    space = Label(root, text="                                       ")
    space.grid(row=0, column=1)

    new_task_box = Entry(root, width=45, textvariable = task_var)
    new_task_box.grid(row=0, column=2, columnspan=50)

    edit_task_box = Entry(root, width=45, textvariable = edited_task)
    edit_task_box.grid(row=1, column=2, columnspan=50)

    new_task_btn = Button(root, text="Lisää Tehtävä", command=new_task)
    new_task_btn.grid(row=2, column=2, padx=2, pady=1, columnspan=1)

    delete_task_btn = Button(root, text="Poista Tehtävä", command=delete_task)
    delete_task_btn.grid(row=2, column=3, padx=2, pady=1, columnspan=1)
    
    edit_task_btn = Button(root, text="Muokkaa Tehtävää", command=edit_task)
    edit_task_btn.grid(row=2, column=4, padx=2, pady=1, columnspan=1)

def new_task():
    global tasks_shown
    task = task_var.get()
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    tasks_shown.destroy()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            logged_in_as TEXT,
            task TEXT
    )''')

    c.execute("INSERT INTO tasks (logged_in_as, task) VALUES (?, ?)", (logged_in_as, task))
    
    conn.commit()
    conn.close()

    display_tasks()

def display_tasks():
    global tasks_shown
    tasklist = []
    global logged_in_as
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    for i in range(0,len(tasks),1):
        if tasks[i][0] == logged_in_as:
            tasklist.append(tasks[i][1])

    tasks_shown = Label(root, text="\n".join(tasklist))
    tasks_shown.grid(row=3, column=2, columnspan=50)

    conn.commit()
    conn.close()            

def delete_task():
    global tasks_shown
    task = task_var.get()
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    tasks_shown.destroy()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            logged_in_as TEXT,
            task TEXT
    )''')

    c.execute("DELETE FROM tasks WHERE (logged_in_as, task) = (?, ?)", (logged_in_as, task))

    conn.commit()
    conn.close()

    display_tasks()

def edit_task():
    global tasks_shown
    edited = edited_task.get()
    task = task_var.get()
    edited = edited_task.get()
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    tasks_shown.destroy()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            logged_in_as TEXT,
            task TEXT
    )''')

    c.execute("DELETE FROM tasks WHERE (logged_in_as, task) = (?, ?)", (logged_in_as, task))

    c.execute("INSERT INTO tasks (logged_in_as, task) VALUES (?, ?)", (logged_in_as, edited))

    conn.commit()
    conn.close()

    display_tasks() 

def logout():
    global tasks_shown, username_box, password_box, login_btn, logout_btn, register_btn, logged_user, space, new_task_box, edit_task_btn, delete_task_btn, new_task_btn

    logged_in_as = ""

    logout_btn.destroy()
    logged_user.destroy()
    space.destroy()
    edit_task_btn.destroy()
    new_task_btn.destroy()
    delete_task_btn.destroy()
    new_task_box.destroy()
    tasks_shown.destroy()

    username_box = Entry(root, width=30, textvariable = username_var)
    username_box.grid(row=0, column=0, columnspan=50, padx=2, pady=1)

    password_box = Entry(root, width=30, textvariable = password_var)
    password_box.grid(row=1, column=0, columnspan=50, padx=2, pady=1)

    login_btn = Button(root, text="Login", command=login_submit)
    login_btn.grid(row=2, column=0, columnspan=1)

    register_btn = Button(root, text="Register", command=register_submit)
    register_btn.grid(row=2, column=1, columnspan=1)

username_box = Entry(root, width=30, textvariable = username_var)
username_box.grid(row=0, column=0, columnspan=50, padx=2, pady=1)

password_box = Entry(root, width=30, textvariable = password_var)
password_box.grid(row=1, column=0, columnspan=50, padx=2, pady=1)

login_btn = Button(root, text="Login", command=login_submit)
login_btn.grid(row=2, column=0, columnspan=1)

register_btn = Button(root, text="Register", command=register_submit)
register_btn.grid(row=2, column=1, columnspan=1)

root.mainloop()