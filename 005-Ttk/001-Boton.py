import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#comparando widgets
ttk.Button(ventana,text="Pulsame ttk").pack(padx=50,pady=50)
tk.Button(ventana,text="Pulsame tk").pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
