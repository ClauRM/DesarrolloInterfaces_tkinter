import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#comparando widgets
ttk.Entry(ventana).pack(padx=50,pady=50)
tk.Entry(ventana).pack(padx=50,pady=50)


ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
