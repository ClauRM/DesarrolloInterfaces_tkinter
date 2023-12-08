import tkinter as tk
from tkinter import ttk

def leerValor():
    print("Obtengo el valor de la entrada:",entrada.get())

ventana = tk.Tk()

entrada = ttk.Entry(ventana)
entrada.pack(padx=20,pady=20)

boton = ttk.Button(ventana,text="Obtener valor", command=leerValor)
boton.pack(padx=20,pady=20)

ventana.mainloop() 
