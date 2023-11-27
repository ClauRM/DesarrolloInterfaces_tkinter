import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ttk.Scale(ventana,from_=0,to=100).pack(padx=50,pady=50)
tk.Scale(ventana,from_=0,to=100,orient=tk.HORIZONTAL).pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
