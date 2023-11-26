import tkinter as tk

def salir():
    ventana.destroy()#la ventana se cierra

ventana = tk.Tk()
barramenu=tk.Menu(ventana)
ventana.config(menu=barramenu)

#MENU ARCHIVO
archivo=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Archivo",menu=archivo)

archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_command(label="Salir",command=salir)

#MENU EDITAR
editar=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Editar",menu=editar)

editar.add_command(label="Deshacer")
editar.add_command(label="Copiar")
editar.add_command(label="Cortar")
editar.add_command(label="Pegar")

#MENU AYUDA
ayuda=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=ayuda)

ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Documentación en líneas")
ayuda.add_command(label="Acerca de")
ayuda.add_command(label="Soporte")


ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
