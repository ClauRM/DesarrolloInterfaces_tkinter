import tkinter as tk
from tkinter import ttk

def saluda():
    print("Has pulsado un botón")

ventana= tk.Tk()

ttk.Button(ventana,text="Pulsa el botón",command=saluda).pack(padx=10,pady=10)

ventana.mainloop()
