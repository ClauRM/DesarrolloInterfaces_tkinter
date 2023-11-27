import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

marco=tk.Frame(ventana,padx=50,pady=50)

#los elementos se agregan al marco
tk.Label(marco,text="Hola mundo desde un Frame").pack(padx=10,pady=10)
tk.Button(marco,text="Esto es un botón").pack(padx=10,pady=10)

#se empaqueta el marco, no la ventana
marco.pack()

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
