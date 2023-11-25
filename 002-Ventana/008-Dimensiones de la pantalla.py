import tkinter as tk

ventana = tk.Tk()
ventana.title("Aprendiendo Tkinter")

anchuraventana = 400
alturaventana = 400

anchurapantalla = ventana.winfo_screenwidth()
alturapantalla = ventana.winfo_screenheight()

esquinax= int (anchurapantalla/2 - anchuraventana/2)
esquinay= int (alturapantalla/2 - alturaventana/2)

##ventana.geometry("400x400+20+20") #resolucion + margen superior + margen izquierdo
ventana.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
