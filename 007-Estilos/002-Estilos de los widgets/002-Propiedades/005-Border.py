import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton',foreground='#11FF00',padding=30,borderwidth=10,relief='raised')

ttk.Button(ventana,text="Pulsa el botón").pack(padx=10,pady=10)

ventana.mainloop()
