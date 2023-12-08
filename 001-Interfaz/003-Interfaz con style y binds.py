import tkinter as tk
from tkinter import ttk

def validarCampo(evento):
    if len(campoNombre.get()) <= 0 or len(campoApellidos.get()) <= 0 or len(campoTelefono.get()) <= 0 or len(campoEmail.get()) <= 0:
        mensajes.config(text="Todos los campos deben tener contenido")
    
def cambiaEstilo():
    try:
        estilo.theme_use(desplegable.get())
        mensajes.config(text="Has cambiado el estilo")
    except:
        mensajes.config(text="Debes deleccionar un estilo de la lista antes de aplicar")

def guardaContacto():
    if len(campoNombre.get()) <= 0 or len(campoApellidos.get()) <= 0 or len(campoTelefono.get()) <= 0 or len(campoEmail.get()) <= 0:
        mensajes.config(text="Se deben completar todos los campos antes de guardar el contacto en la agenda")
    else:
        numeroContactos = len(tabla.get_children())#numero de elementos en la tabla
        n = numeroContactos +1
        elementoN = f'elemento{numeroContactos + 1}'
        ContactoN = f'Contacto{numeroContactos + 1}'
        #aniadir nuevo contacto
        tabla.insert('',n, elementoN, text=ContactoN, values=(
            campoNombre.get(), campoApellidos.get(), campoTelefono.get(), campoEmail.get()))
        mensajes.config(text="Contacto añadido correctamente")

def limpiaFormulario():
    campoNombre.delete(0,tk.END)
    campoApellidos.delete(0,tk.END)
    campoTelefono.delete(0,tk.END)
    campoEmail.delete(0,tk.END)
    mensajes.config(text="")
    
def seleccionaElemento(evento):
    seleccionado = tabla.focus() #elemento que se ha seleccionado
    valores = tabla.item(seleccionado,'values') #valores del elemento seleccionado
    mensajes.config(text=f'Contacto seleccionado: {valores}') #formateo de valores    

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
campoNombre.bind("<FocusOut>", validarCampo)
campoApellidos.bind("<FocusOut>", validarCampo)
campoTelefono.bind("<FocusOut>", validarCampo)
campoEmail.bind("<FocusOut>", validarCampo)

#BOTON GUARDAR Y LIMPIAR
botonGuardar = ttk.Button(ventana,text="Guardar contacto",command=guardaContacto)
botonGuardar.grid(row=4, column=1, pady=10)

botonLimpiar = ttk.Button(ventana,text="Limpiar formulario",command=limpiaFormulario)
botonLimpiar.grid(row=4, column=2, pady=10)

mensajes = ttk.Label(ventana,text="")
mensajes.grid(row=5, column=0, columnspan=4)

#TABLA
tabla = ttk.Treeview(ventana,columns=('nombre','apellidos','telefono','email'))
tabla.heading("#0",text="Identificador")
tabla.heading("nombre",text="Nombre")
tabla.heading("apellidos",text="Apellidos")
tabla.heading("telefono",text="Teléfono")
tabla.heading("email",text="Correo electronico")

tabla.insert('','0','elemento1',text='Contacto1', values=("Claudia","Rubio Menco","12345678","claudia@email.com"))
tabla.insert('','1','elemento2',text='Contacto2', values=("Mateo","Rodriguez Perez", "87654321","mateo@email.com"))

tabla.grid(row=6, column=0, columnspan=4, padx=50, pady=10)

tabla.bind('<<TreeviewSelect>>',seleccionaElemento)

#CAMBIAR EL ESTILO
desplegable = ttk.Combobox(ventana,values=estilo.theme_names())
desplegable.grid(row=7, column=3, padx=10, pady=10)

botonCambiar = ttk.Button(ventana,text="Aplica el estilo",command=cambiaEstilo)
botonCambiar.grid(row=8, column=3, padx=10, pady=10)

ventana.mainloop()
