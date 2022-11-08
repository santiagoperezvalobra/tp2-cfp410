import random
from random import choice
import tkinter as tk
from tkinter import ttk
from tkinter import *

try:
    ANCHO=500
    ALTO=400

    app = tk.Tk()
    app.title("Sorteo")
    app.config(width=ANCHO, height=ALTO)
    app.resizable(0, 0) 

    text1 = ttk.Label(text= "Ingrese nombre del participante: ")
    text1.place(x=20,y=20)
    text_inputVar = tk.StringVar()
    text_input = ttk.Entry(width=40,textvariable=text_inputVar)
    text_input.place(x=240, y=20)
    text_input.focus_set()
       
    textoo = tk.StringVar()
    text2 = ttk.Label(app,textvariable=textoo)
    text2.place(x=20,y=100)

    participantes = []

    lista = Listbox(app, width= 50)
    lista.place(x=160, y=140)

    def inscripciones(*args):
        participante = text_inputVar.get()
        participantes.append(participante)
        lista.insert(tk.END, participante)
        text_inputVar.set('')    

    btn_gen = ttk.Button(text="Anotar", command=inscripciones)
    btn_gen.place(x=40,y=60)

    def sorteo():
        winner = random.choice(participantes)
        textoo.set(f"El ganador es: {winner}")

    btn_gen = ttk.Button(text="Sorteo", command=sorteo)
    btn_gen.place(x=120,y=60)

    # Bind the Enter Key to the window
    app.bind('<Return>', inscripciones)

    def nuevo_sorteo():
        participantes.clear()
        lista.delete(0,END)
        textoo.set("")
    btn_gen = ttk.Button(text="Nuevo sorteo", command=nuevo_sorteo)
    btn_gen.place(x=200,y=60)
    
    app.mainloop()

except ImportError as e:
    print(f"Error al importar el módulo.\nERROR: {e}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado.\nERROR: {e}")
