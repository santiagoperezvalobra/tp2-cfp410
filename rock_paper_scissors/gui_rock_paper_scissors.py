import tkinter as tk
from tkinter import ttk

try:
    import rock_paper_scissors

    # Dimensiones de la ventana (en píxeles)
    ANCHO=500
    ALTO=400

    # Definimos app
    app = tk.Tk()
    app.title("Piedra, Papel o Tijeras")
    app.config(width=ANCHO, height=ALTO)
    app.resizable(0, 0) # Para que la ventana no pueda redimensionarse

    # Definimos un texto
    text1 = ttk.Label(text=f"Elija una opción (en numeros):\n1) Piedra\n2) Papel\n3) Tijera.\n")
    # Posición del texto
    text1.place(x=20,y=20)

    # Definimos input
    text_input = ttk.Entry(width=4)
    # Posición del input
    text_input.place(x=270, y=20)

    # Variable donde se guardará la eleccion.
    choice = tk.StringVar()

    def generador():
        try:
            eleccion = abs(int(text_input.get()))
            if (1 <= int(eleccion) <= 3):
                choice.set(rock_paper_scissors.rock_paper_scissors(eleccion))
            else:
                raise Exception

        except Exception as e:
            # Inserta un texto en el StringVar.
            # Si da error al convertir a int lo ingresado, mostrará este mensaje de error.
            choice.set("¡ERROR!. Ingrese un número válido.")
            print(f"ERROR: {e}")

    # El botón para jugar
    btn_gen = ttk.Button(text="Jugar", command=generador)
    # La ubicación del botón
    btn_gen.place(x=60,y=80)

    #Texto para el resultado
    text2 = ttk.Label(app, textvariable=choice)
    # Posición del texto
    text2.place(x=20,y=120)
    # Loop de la aplicación
    app.mainloop()

except ImportError as e:
    print(f"Error al importar el módulo piedra papel o tijeras.\nERROR: {e}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado.\nERROR: {e}")
