import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ttk.Progressbar(ventana, length=200, mode='indeterminate').pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
