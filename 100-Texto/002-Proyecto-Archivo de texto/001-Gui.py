import tkinter as tk

ventana = tk.Tk()

archivo= open("estructura.txt","r")
print(archivo)

###leer archivo de texto
##for linea in archivo:
##    print(linea)

#o bien se puede leer de la siguiente forma
lineas = archivo.readlines()

for linea in lineas:
    print(linea)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
