import tkinter as tk
from tkinter import ttk #acceso a los widgets tematicos (themed tkinter)

def salir():
    ventana.destroy()#la ventana se cierra

def nuevo():
    entrada.delete(0, tk.END)

def acerca():
    tk.Label(ventana,text="Creado por Claudia Rubio (C) 2023",font=negrita).pack(pady=20)

def convertir():
    temperatura = entrada.get()
    print("La temperatura marcada es:",temperatura,"ºC")
    #formula (0 °C × 9 / 5) + 32  = 32 ºF
    try:
        fahrenheit = (int(temperatura) *9/5)+32
        print("La temperatura en ºF es",fahrenheit)
        if int(temperatura) <=10:
            print("¡Uff, hace un poco de frío!")
        if int(temperatura) >10 and int(temperatura) <=20:
            print("¡Ya no hace tanto frío!")
        if int(temperatura) >20 and int(temperatura) <=30:
            print("¡Una temperatura bastante buena!")
        if int(temperatura) >30:
            print("¡Empieza a hacer algo de calor!")
    except Exception as e:
        print("Ocurrió un error:", e)


ventana = tk.Tk()
ventana.geometry("400x250+20+20")
ventana.title("Convertidor de temperatura")
ventana.iconbitmap("temperatura.ico")

#BARRA DE MENU
barramenu=tk.Menu(ventana)
ventana.config(menu=barramenu)

#MENU ARCHIVO
archivo=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Archivo",menu=archivo)

archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_command(label="Salir",command=salir)

#MENU AYUDA
ayuda=tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=ayuda)

ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Documentación en línea")
ayuda.add_command(label="Acerca de",command=acerca)

#WIDGETS DE VENTANA
negrita = ('Arial', 10, 'bold')
tk.Label(ventana,text="Hola!",font=negrita).pack(pady=5)
tk.Label(ventana,text="Bienvenido al convertidor de temperatura!").pack(pady=5)
ttk.Separator(ventana, orient="horizontal").pack(fill="x", pady=5)
tk.Label(ventana,text="Introduce la temperatura en grados Celsius (ºC):").pack(padx=20,anchor="w")
entrada = tk.Entry(ventana)
entrada.pack(padx=20,pady=5,anchor="w")
tk.Button(ventana,text="Convertir",command=convertir).pack()

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
