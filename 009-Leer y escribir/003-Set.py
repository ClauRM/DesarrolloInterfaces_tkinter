import tkinter as tk
from tkinter import ttk

def leerValor():
    print("Obtengo el valor de la entrada:",entrada.get())

def ponerValor():
    entrada.delete(0,tk.END)
    entrada.insert(0,"Nuevo Valor")

ventana = tk.Tk()

entrada = ttk.Entry(ventana)
entrada.pack(padx=20,pady=20)

boton = ttk.Button(ventana,text="Obtener valor", command=leerValor)
boton.pack(padx=20,pady=20)

boton2 = ttk.Button(ventana,text="Pon el valor", command=ponerValor)
boton2.pack(padx=20,pady=20)

ventana.mainloop() 
