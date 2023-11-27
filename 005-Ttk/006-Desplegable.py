import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ttk.Combobox(ventana, values=['manzana ttk','pera ttk','sandia ttk']).pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
