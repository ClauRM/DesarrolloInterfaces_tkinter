import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton',foreground='red')

ttk.Button(ventana,text="Púlsame").pack(padx=10,pady=10)

ventana.mainloop()
