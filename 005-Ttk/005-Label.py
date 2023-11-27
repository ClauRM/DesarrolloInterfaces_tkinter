import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#comparando widgets
ttk.Label(ventana, text="Hola mundo desde ttk").pack(padx=50,pady=50)
tk.Label(ventana, text="Hola mundo desde tk").pack(padx=50,pady=50)


ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
