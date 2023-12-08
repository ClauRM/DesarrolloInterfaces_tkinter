import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton',padding=10,width=50,height=20)

ttk.Button(ventana,text="Pulsa el botón").pack(padx=10,pady=10)

ventana.mainloop()
