import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

estilo = ttk.Style()
print(estilo.theme_names())
estilo.theme_use("clam")

tk.Button(ventana,text="Boton de tk con estilo").pack(padx=10,pady=10)
ttk.Button(ventana,text="Boton de ttk con estilo").pack(padx=10,pady=10)

ventana.mainloop()
