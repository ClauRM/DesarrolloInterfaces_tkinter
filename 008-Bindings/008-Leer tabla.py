import tkinter as tk
from tkinter import ttk

def seleccionaElemento(evento):
    seleccionado = arbol.focus()
    print(seleccionado)
    valores = arbol.item(seleccionado,'values')
    print(valores)

ventana = tk.Tk()

arbol = ttk.Treeview(ventana,columns=('nombre','apellidos','email'))
arbol.heading("#0",text="Identificador")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electronico")

arbol.insert('','0','elemento1',text='Cliente1', values=("Claudia","Rubio Menco", "claudia@email.com"))
arbol.insert('','1','elemento2',text='Cliente2', values=("Mateo","Rodriguez Perez", "mateo@email.com"))

arbol.pack(padx=50,pady=50)

arbol.bind('<<TreeviewSelect>>',seleccionaElemento)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
