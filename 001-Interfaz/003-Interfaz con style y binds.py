import tkinter as tk
from tkinter import ttk

def validaciones(evento):
    pass
    
def cambiaEstilo():
    print("Cambia el estilo")
    estilo.theme_use(desplegable.get())

def guardaContacto():
    pass
    
def seleccionaElemento(evento):
    seleccionado = arbol.focus()
    print(seleccionado)
    valores = arbol.item(seleccionado,'values')
    print(valores)
    

#VENTANA Y ESTILOS
ventana = tk.Tk()
ventana.title("Agenda")
ventana.iconbitmap("agenda.ico")
estilo = ttk.Style()
estilo.configure("TButton", padding=3, relief="flat",background="#252657")
estilo.configure("TLabel",foreground="#252657",font=('Helvetica',11))
estilo.configure('TEntry',padding=5)

#INTERFAZ DE USUARIO
titulo=ttk.Label(ventana,text="AGENDA DE CONTACTOS")
titulo.grid(row=0, column=0, columnspan=4)
separador = ttk.Separator(ventana, orient='horizontal')
separador.grid(row=1, column=0, columnspan=4, sticky='ew', pady=10)

ttk.Label(ventana,text="Nombre").grid(row=2, column=0)
ttk.Label(ventana,text="Apellidos").grid(row=2, column=1)
ttk.Label(ventana,text="Telefono").grid(row=2, column=2)
ttk.Label(ventana,text="Email").grid(row=2, column=3)

#FORMULARIO
campoNombre = ttk.Entry(ventana,)
campoApellidos = ttk.Entry(ventana)
campoTelefono = ttk.Entry(ventana)
campoEmail = ttk.Entry(ventana)

campoNombre.grid(row=3, column=0)
campoApellidos.grid(row=3, column=1)
campoTelefono.grid(row=3, column=2)
campoEmail.grid(row=3, column=3)

#LISTENER FORMULARIO


#BOTON GUARDAR
botonGuardar = ttk.Button(ventana,text="Guardar contacto",command=guardaContacto)
botonGuardar.grid(row=4, column=0, columnspan=4, pady=10)

mensajes = ttk.Label(ventana,text="mensajes")
mensajes.grid(row=5, column=0, columnspan=4)

#TABLA
arbol = ttk.Treeview(ventana,columns=('nombre','apellidos','telefono','email'))
arbol.heading("#0",text="Identificador")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("telefono",text="Teléfono")
arbol.heading("email",text="Correo electronico")

arbol.insert('','0','elemento1',text='Cliente1', values=("Claudia","Rubio Menco","12345678","claudia@email.com"))
arbol.insert('','1','elemento2',text='Cliente2', values=("Mateo","Rodriguez Perez", "87654321","mateo@email.com"))

arbol.grid(row=6, column=0, columnspan=4, padx=50, pady=10)

arbol.bind('<<TreeviewSelect>>',seleccionaElemento)

#CAMBIAR EL ESTILO
desplegable = ttk.Combobox(ventana,values=estilo.theme_names())
desplegable.grid(row=7, column=3, padx=10, pady=10)

botonCambiar = ttk.Button(ventana,text="Aplica el estilo",command=cambiaEstilo)
botonCambiar.grid(row=8, column=3, padx=10, pady=10)

ventana.mainloop()
