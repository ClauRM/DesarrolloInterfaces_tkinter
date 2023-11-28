import tkinter as tk

ventana = tk.Tk()

archivo= open("estructura.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    elemento = linea.strip()
    if elemento == "entrada":
        tk.Entry(ventana).pack()
    elif elemento == "etiqueta":
        tk.Label(ventana,text="Esto es una etiqueta").pack()
    elif elemento == "boton":
        tk.Button(ventana, text="Esto es un botón").pack()

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
