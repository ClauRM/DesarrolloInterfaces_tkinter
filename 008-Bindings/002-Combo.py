import tkinter as tk
from tkinter import ttk

def saluda(evento):
    print("Has cambiado la opción del selector a:",desplegable.get())

ventana= tk.Tk()

desplegable=ttk.Combobox(ventana,values=['uno','dos','tres','cuatro','cinco'])
desplegable.pack(padx=10,pady=10)

desplegable.bind('<<ComboboxSelected>>',saluda)#codigo de que es lo que ocurre

ventana.mainloop()
