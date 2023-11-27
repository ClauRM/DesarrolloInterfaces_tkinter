import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

etiqueta1= tk.Label(ventana,text="Etiqueta1")
etiqueta2= tk.Label(ventana,text="Etiqueta2")
etiqueta3= tk.Label(ventana,text="Etiqueta3")
etiqueta4= tk.Label(ventana,text="Etiqueta4")

etiqueta1.grid(row=0,column=0,padx=10,pady=10)
etiqueta2.grid(row=0,column=1,padx=10,pady=10)
etiqueta3.grid(row=1,column=0,padx=10,pady=10)
etiqueta4.grid(row=1,column=1,padx=10,pady=10)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
