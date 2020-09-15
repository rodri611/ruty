from flask import Flask, Markup, render_template
import mysql.connector
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="ruty")

mycursor = mydb.cursor()

query = "INSERT INTO temperatura (temp) VALUES (%s)"
values = (float(40))
cursor.execute(query, values)
db.commit()

root = tk.Tk()

w = tk.Label(root, text="Ingrese Temperatura")
w.pack()
w.place(x=55, y=10)

root.config(width=250, height=200)

# Crear caja de texto.
entry = ttk.Entry(root)

# Posicionarla en la ventana.
entry.place(x=50, y=50)

button = tk.Button(root, text='Insertar', width=17, command=root.destroy)
button.pack()
button.place(x=50, y=80)

root.mainloop()
