#abrir ventana cmd, ejecutar pip install bs4
from bs4 import BeautifulSoup
import tkinter as tk

ventana = tk.Tk()

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"lxml")

for campo in xml.find_all("campo"):
    print(campo)
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    print(texto)

    if tipo == "entrada":
        tk.Entry(ventana).pack(padx=10,pady=10)
    elif tipo == "etiqueta":
        tk.Label(ventana,text=texto).pack(padx=10,pady=10)
    elif tipo == "boton":
        tk.Button(ventana, text=texto).pack(padx=10,pady=10)
    

ventana.mainloop()
