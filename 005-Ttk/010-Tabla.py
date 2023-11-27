import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

arbol = ttk.Treeview(ventana,columns=('nombre','apellidos','email'))
arbol.heading("#0",text="Identificador")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electronico")


arbol.pack(padx=50,pady=50)


ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
