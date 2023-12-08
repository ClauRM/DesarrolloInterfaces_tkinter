import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()

estilo = ttk.Style()
estilo.configure('TLabel',foreground='#FFFFFF',background='blue',padding=30)

ttk.Label(ventana,text="Texto del prueba").pack(padx=10,pady=10)

ventana.mainloop()
