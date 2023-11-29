import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup #libreria xml

#FUNCIONES DEL MENU
def seleccionar_opcion(opcion):
    if opcion == "nuevo":
        nuevo()
    elif opcion == "abrir":
        # codigo
        pass
    elif opcion == "guardar":
        # codigo
        pass
    elif opcion == "salir":
        salir()
    elif opcion == "ayuda":
        # codigo
        pass
    elif opcion == "documentacion":
        # codigo
        pass
    elif opcion == "acerca":
        acerca()

def salir():
    ventana.destroy()#la ventana se cierra

def nuevo():
    entrada.delete(0, tk.END)

def acerca():
    tk.Label(ventana,text="Creado por Claudia Rubio (C) 2023",font=negrita).pack(pady=10)

#FUNCION DE LA APLICACION
def convertir():
    temperatura = entrada.get()
    mensaje=""
    try:
        #formula (0 °C × 9 / 5) + 32  = 32 ºF
        fahrenheit = (int(temperatura) *9/5)+32
        salida = "La temperatura en ºF es "+str(fahrenheit)
        tk.Label(ventana,text=salida,font=negrita).pack()
        if int(temperatura) <=10:
            mensaje="¡Uff, hace un poco de frío!"
        if int(temperatura) >10 and int(temperatura) <=20:
            mensaje="¡Ya no hace tanto frío!"
        if int(temperatura) >20 and int(temperatura) <=30:
            mensaje="¡Una temperatura bastante buena!"
        if int(temperatura) >30:
            mensaje="¡Empieza a hacer algo de calor!"
    except Exception as e:
        print("Ocurrió un error:", e)
        mensaje= "No has marcado un valor numerico"
    finally:    
        tk.Label(ventana,text=mensaje).pack()
    
#VENTANA
ventana = tk.Tk()
ventana.geometry("400x700+20+20")
ventana.title("Convertidor de temperatura")
ventana.iconbitmap("temperatura.ico")

barramenu=tk.Menu(ventana)
ventana.config(menu=barramenu)

#LEER XML
archivo = open("temperatura.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")

#FORMATOS
negrita = ('Arial', 10, 'bold')
margenes = {'padx': 10, 'pady': 10}

#CAPTURAR CAMPOS XML
for menu in xml.find_all("menu"):
    nombremenu = menu.get("texto")
    desplegable = tk.Menu(barramenu, tearoff=0)

    for menuitem in menu.find_all("menuitem"):
        nombreitem = menuitem.get("texto")
        desplegable.add_command(label=nombreitem.capitalize(), command=lambda item=nombreitem: seleccionar_opcion(item))

    barramenu.add_cascade(label=nombremenu.capitalize(), menu=desplegable)


for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    formato = campo.get("formato")
    alineacion = campo.get("alineacion")
    
    if tipo == "entrada":
        entrada = ttk.Entry(ventana)
        if alineacion == "izquierda":
            entrada.pack(**margenes,anchor="w") #** para desempaquetar
        else:
            entrada.pack(**margenes)
    elif tipo == "label":
        if formato == "negrita":
            ttk.Label(ventana,text=texto, font=negrita).pack(**margenes)
        elif alineacion == "izquierda":
            ttk.Label(ventana,text=texto).pack(**margenes, anchor="w")
        elif formato != "negrita" and alineacion != "izquierda":
            ttk.Label(ventana,text=texto).pack(**margenes)       
    elif tipo == "boton":
        ttk.Button(ventana, text=texto, command=convertir).pack(**margenes)
    elif tipo == "separador":
        ttk.Separator(ventana, orient="horizontal").pack(fill="x", pady=5)

ventana.mainloop()
