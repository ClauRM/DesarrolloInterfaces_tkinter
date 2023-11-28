import tkinter as tk

ventana = tk.Tk()

archivo= open("estructura.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    contenido = linea.strip().split(",")
    elemento=contenido[0]
        
    if elemento == "entrada":
        tk.Entry(ventana).pack(padx=10,pady=10)
    elif elemento == "etiqueta":
        tk.Label(ventana,text=contenido[1]).pack(padx=10,pady=10)
    elif elemento == "boton":
        tk.Button(ventana, text=contenido[1]).pack(padx=10,pady=10)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
