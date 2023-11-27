import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#comparando widgets
ttk.Checkbutton(ventana, text="Esta es una opción ttk").pack(padx=50,pady=50)
tk.Checkbutton(ventana, text="Esta es una opción tk").pack(padx=50,pady=50)


ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
