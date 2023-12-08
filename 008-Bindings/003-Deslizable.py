import tkinter as tk
from tkinter import ttk

def dimeValor(evento):
    print("Valor seleccionado:",deslizable.get())
    
ventana = tk.Tk()

deslizable = ttk.Scale(ventana,from_=0,to=100)
deslizable.pack(padx=20,pady=20)

deslizable.bind('<ButtonRelease>',dimeValor)

ventana.mainloop()
