import tkinter as tk

ventana = tk.Tk()

def saluda():
    print("Has pulsado un boton")

tk.Button(ventana,text="Hola Mundo desde Tkinter", command=saluda).pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
