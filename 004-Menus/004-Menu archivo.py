import tkinter as tk

ventana = tk.Tk()
barramenu=tk.Menu(ventana)
ventana.config(menu=barramenu)
archivo=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Archivo",menu=archivo)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
