import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventanapartida = tk.PanedWindow(ventana,orient=tk.HORIZONTAL)
marco1= tk.Frame(ventanapartida, background="red")
marco2= tk.Frame(ventanapartida, background="blue")

ventanapartida.add(marco1)
ventanapartida.add(marco2)

ventanapartida.pack(fill=tk.BOTH,expand=True)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
