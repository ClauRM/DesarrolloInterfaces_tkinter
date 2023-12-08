import tkinter as tk
from tkinter import ttk

def cambiaEstilo():
    print("Cambia el estilo")
    estilo.theme_use(desplegable.get())

ventana = tk.Tk()

estilo = ttk.Style()
print(estilo.theme_names())
estilo.theme_use("clam")

desplegable = ttk.Combobox(ventana,values=estilo.theme_names())
desplegable.pack(padx=10,pady=10)

botonCambiar = ttk.Button(ventana,text="Applica el estilo",command=cambiaEstilo)
botonCambiar.pack(padx=10,pady=10)

tk.Button(ventana,text="Boton de tk con estilo").pack(padx=10,pady=10)
ttk.Button(ventana,text="Boton de ttk con estilo").pack(padx=10,pady=10)

ventana.mainloop()
