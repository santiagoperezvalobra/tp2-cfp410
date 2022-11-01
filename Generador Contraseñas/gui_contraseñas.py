import tkinter as tk
from tkinter import ttk

try:
    import generador_contraseñas

    # El máximo posible de contraseña. Para que no pueda hacerse una contraseña de infinitos caracteres.
    MAX_LENGTH = 32
    MIN_LENGTH = 5
     # Dimensiones de la ventana (en píxeles)
    ANCHO=500 
    ALTO=200

    # Definimos app
    app = tk.Tk()
    app.title("Generador de contraseñas seguras")
    app.config(width=ANCHO, height=ALTO)
    app.resizable(0, 0) # Para que la ventana no pueda redimensionarse

    # Definimos un texto
    text1 = ttk.Label(text=f"Longitud de la contraseña (Max {MAX_LENGTH}, Min {MIN_LENGTH}):")
    # Posición del texto
    text1.place(x=20,y=20) 

    # Definimos input
    text_input = ttk.Entry(width=4)
    # Posición del input
    text_input.place(x=270, y=20)

    # Variable donde se guardará la contraseña.
    contra = tk.StringVar()

    # Texto para avisar que la contraseña se almacenó en el portapapeles
    msg = tk.StringVar()

    def clip(text):
        '''
        Copia el parámetro enviado 'text' al portapapeles
        '''
        app.clipboard_clear()
        app.clipboard_append(text)


    def generator():
        '''
        Toma la longitud de la contraseña en el input y la envía a la función que genera la contraseña
        '''
        # Si se encuentra contenido en el input
        
        try:
            cantidad = abs(int(text_input.get())) # abs para convertir negativos en números válidos
            # No hubo excepción. Se espera que muestre la contraseña de longitud 'cantidad'    
            print(cantidad)
            if cantidad <= MAX_LENGTH and cantidad>=MIN_LENGTH:
                contra.set(generador_contraseñas.generador_contraseñas(cantidad-4))
                msg.set("Se ha guardado la contraseña completa al portapapeles.")
                clip(contra.get()) # Copia la contraseña al portapapeles
            else:
                raise Exception


        except Exception as e:
            # Inserta un texto en el StringVar.
            # Si da error al convertir a int lo ingresado, mostrará este mensaje de error.
            contra.set("¡ERROR!. Ingrese un número válido.")
            msg.set("")
            print(f"ERROR: {e}")

    # El botón para generar contraseñas
    btn_gen = ttk.Button(text="Generar contraseña segura", command=generator)
    # La ubicación del botón
    btn_gen.place(x=20,y=60)

    '''
    El label que contendrá la contraseña
    Observe el parámetro 'textvariable = contra'. Contra es el StringVar. Por lo tanto, el texto cambiará automáticamente cuando se cambie
    el StringVar
    '''
    text_contra = ttk.Label(app, textvariable = contra, font=("Courier New", 12))
    # Ubicación de la contraseña
    text_contra.place(x=20,y=110)

    # Mensaje para avisar que la contraseña se guardó en el portapapeles
    text_msg_porta = ttk.Label(app, textvariable = msg)
    # Ubicación del mensaje para avisar que la contraseña se guardó en el portapapeles
    text_msg_porta.place(x=20,y=160)

    # Loop de la aplicación
    app.mainloop()

except ImportError as e:
    print(f"Error al importar el módulo generador de contraseñas.\nERROR: {e}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado.\nERROR: {e}")
