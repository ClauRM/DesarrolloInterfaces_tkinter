import tkinter as tk

ventana = tk.Tk()
barramenu=tk.Menu(ventana)
ventana.config(menu=barramenu)
archivo=tk.Menu(barramenu,tearoff=1) #tearoff =1 se pueden sacar las barras de menu
barramenu.add_cascade(label="Archivo",menu=archivo)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
